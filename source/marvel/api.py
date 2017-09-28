import time
import hashlib
import requests
import json


class MarvelAPI:
    base_endpoint = 'https://gateway.marvel.com'
    public_key = 'XXX'
    private_key = 'XXX'

    def _dorequest(self, endpoint):
        ts = str(int(time.time()))
        api_hash = hashlib.md5((ts + self.private_key + self.public_key).encode('utf-8')).hexdigest()
        params = {
            'ts': ts,
            'apikey': self.public_key,
            'hash': api_hash
        }
        url = '%s%s' % (self.base_endpoint, endpoint)
        r = requests.get(url, params)
        print(r.status_code)
        print(json.loads(r.text))
        return r

    def characters(self):
        return self._dorequest('/v1/public/characters')

    def comics(self):
        return self._dorequest('/v1/public/comics')
