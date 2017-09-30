import hashlib
import json
import os
import time

import requests
import logging

log = logging.getLogger('marvel')
base_endpoint = 'https://gateway.marvel.com'
public_key = os.environ.get('MARVEL_PUBLIC_KEY')
private_key = os.environ.get('MARVEL_PRIVATE_KEY')


class MarvelRequest(object):

    def characters(self, page=1):
        r = self.get('/v1/public/characters', page)
        return json.loads(r.text)['data']['results']

    def get(self, endpoint, page, page_size=100):
        ts = str(int(time.time()))
        api_hash = hashlib.md5((ts + private_key + public_key).encode('utf-8')).hexdigest()
        params = {
            'ts': ts,
            'apikey': public_key,
            'hash': api_hash,
            'offset': (page-1) * page_size,
            'limit': page_size
        }
        url = '%s%s' % (base_endpoint, endpoint)
        r = requests.get(url, params)
        return r
