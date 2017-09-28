import time
import hashlib
import requests


class MarvelAPI:
    base_endpoint = 'https://gateway.marvel.com'
    public_key = 'XXX'
    private_key = 'YYY'

    def characters(self):
        end_point = '/v1/public/characters'
        ts = str(int(time.time()))

        api_hash = hashlib.md5((ts + self.private_key + self.public_key).encode('utf-8')).hexdigest()
        params = {
            'ts': ts,
            'apikey': self.public_key,
            'hash': api_hash
        }

        url = '%s%s' % (self.base_endpoint, end_point)

        r = requests.get(url, params)
        print(r.status_code)
        print(r.content)
        return r

        #         """
        # ts = str(int(time.time()))
        # url = self.api + endpoint
        #
        # params = {
        #     'ts': ts,
        #     'apikey': self.public_key,
        #     'hash': md5(ts + self.private_key + self.public_key).hexdigest(),
        # }
        #
        # # if additional params were passed, update the default params
        # if additional_params is not None:
        #     params.update(additional_params)
        #
        # return requests.get(url, params)
        #
        #
        # # url = self.api + endpoint
        #
        # # params = {
        # #     'ts': ts,
        # #     'apikey': self.public_key,
        # #     'hash': md5(ts + self.private_key + self.public_key).hexdigest(),
        # # }
        # #
        # #
        # # GET
