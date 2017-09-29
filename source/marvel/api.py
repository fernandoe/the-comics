import hashlib
import json
import os
import time

import requests
import logging

log = logging.getLogger('marvel')


#
# class Client:
#     count = 0
#
#     base_endpoint = 'https://gateway.marvel.com'
#
#     public_key = os.environ.get('MARVEL_PUBLIC_KEY')
#     private_key = os.environ.get('MARVEL_PRIVATE_KEY')
#
#     def request(self, endpoint):
#         ts = str(int(time.time()))
#         api_hash = hashlib.md5((ts + self.private_key + self.public_key).encode('utf-8')).hexdigest()
#         params = {
#             'ts': ts,
#             'apikey': self.public_key,
#             'hash': api_hash
#         }
#         url = '%s%s' % (self.base_endpoint, endpoint)
#         result = []
#         items = 0
#         do
#
#         r = requests.get(url, params)
#         print(r.text)
#         return json.loads(r.text)['data']['results']
#
#
# class MarvelAPIIterable(object):
#     def __init__(self, values):
#         # log.debug('__init__')
#         self.values = values
#         self.location = 0
#
#     def __iter__(self):
#         log.debug('__iter__')
#         return self
#
#     def next(self):
#         log.debug('next')
#         if self.location == len(self.values):
#             raise StopIteration
#         value = self.values[self.location]
#         self.location += 1
#         return value
#
# class MarvelAPIIterable:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self):
#         print('__init__')
#         self.page_size = 100
#         self.page_objects = None
#         # self.data = data
#         # self.index = len(data)
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         if self.page_objects == None:
#
#
#
#         print('__next__')
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# def dorequest


class MarvelAPI:
    base_endpoint = 'https://gateway.marvel.com'

    public_key = os.environ.get('MARVEL_PUBLIC_KEY')
    private_key = os.environ.get('MARVEL_PRIVATE_KEY')

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
        return json.loads(r.text)['data']['results']

    def characters(self, identifier=None):
        if identifier:
            return self._dorequest('/v1/public/characters/{identifier}'.format(identifier=identifier))
        else:
            return self._dorequest('/v1/public/characters')

    def comics(self):
        return self._dorequest('/v1/public/comics')

    def stories_by_character(self, identifier):
        return self._dorequest('/v1/public/characters/{identifier}/stories'.format(identifier=identifier))
