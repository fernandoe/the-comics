import hashlib
import json
import logging
import os
import time

import redis
import requests

from marvel.decorator import cached

r = redis.from_url(os.environ.get("REDIS_URL", 'redis://localhost'))
log = logging.getLogger('marvel')
base_endpoint = 'https://gateway.marvel.com'
public_key = os.environ.get('MARVEL_PUBLIC_KEY')
private_key = os.environ.get('MARVEL_PRIVATE_KEY')


class MarvelRequest(object):

    @cached
    def characters(self, identifier=None, page=1):
        if identifier:
            status, result = self.get('/v1/public/characters/%s' % identifier, page)
            return json.loads(result)['data']['results'][0]
        else:
            status, result = self.get('/v1/public/characters', page)
            return json.loads(result)['data']['results']

    @cached
    def characters_by_comic(self, identifier, page=1):
        status, result = self.get('/v1/public/characters', page=page, extra_params={'comics': identifier})
        return json.loads(result)['data']['results']

    def stories_by_character(self, identifier, page=1):
        status, result = self.get('/v1/public/characters/{identifier}/stories'.format(identifier=identifier), page)
        return json.loads(result)['data']['results']

    @cached
    def comics_by_character(self, identifier, page=1):
        status, result = self.get('/v1/public/characters/{identifier}/comics'.format(identifier=identifier), page)
        return json.loads(result)['data']['results']

    def get(self, endpoint, page=1, page_size=100, extra_params=None):
        log.info("Get endpoint={endpoint}, page={page}, page_size={page_size}, extra_params={extra_params}"
                 .format(endpoint=endpoint, page=page, page_size=page_size, extra_params=extra_params))
        ts = str(int(time.time()))
        api_hash = hashlib.md5((ts + private_key + public_key).encode('utf-8')).hexdigest()
        params = {
            'ts': ts,
            'apikey': public_key,
            'hash': api_hash,
            'offset': (page - 1) * page_size,
            'limit': page_size
        }
        if extra_params:
            params.update(extra_params)
        url = '%s%s' % (base_endpoint, endpoint)
        key = self.build_key(endpoint, params)
        headers = {
            'If-None-Match': r.get('TC:MARVEL:ETAG:{KEY}:ETAG'.format(KEY=key))
        }
        result = requests.get(url, params, headers=headers)
        if result.status_code == 200:
            self.store_on_cache(key, result)
        elif result.status_code == 304:
            log.info('Returning from cache, 304 status code')
            return result.status_code, r.get('TC:MARVEL:ETAG:{KEY}:JSON'.format(KEY=key))
        return result.status_code, result.text

    def store_on_cache(self, key, request):
        r.set('TC:MARVEL:ETAG:{KEY}:ETAG'.format(KEY=key), request.json()['etag'])
        r.set('TC:MARVEL:ETAG:{KEY}:JSON'.format(KEY=key), request.text)

    def build_key(self, endpoint, params={}):
        params_copy = params.copy()
        del params_copy['ts']
        del params_copy['apikey']
        del params_copy['hash']
        result = endpoint
        for key in sorted(params_copy):
            result = '%s:%s:%s' % (result, key, params_copy[key])
        return result
