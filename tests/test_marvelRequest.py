import json
from unittest import TestCase
from marvel.request import MarvelRequest
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)


class TestMarvelRequest(TestCase):
    def setUp(self):
        r.flushall()

    def test_characters(self):
        response = MarvelRequest().characters()
        assert 100 == len(response)

    def test_get_page_size(self):
        endpoint = '/v1/public/characters'
        status, response = MarvelRequest().get(endpoint, 1, 5)
        assert 200 == status
        data = json.loads(response)
        assert 5 == len(data['data']['results'])

    def test_get_page_size_default(self):
        endpoint = '/v1/public/characters'
        status, response = MarvelRequest().get(endpoint, 1)
        assert 200 == status
        data = json.loads(response)
        assert 100 == len(data['data']['results'])

    def test_get_pagination(self):
        endpoint = '/v1/public/characters'
        status, response = MarvelRequest().get(endpoint, 1, 9)
        pages = json.loads(response)
        assert 0 == pages['data']['offset']
        assert 9 == pages['data']['limit']
        assert 9 == pages['data']['count']

        status, response = MarvelRequest().get(endpoint, 1, 3)
        page1 = json.loads(response)
        assert 0 == page1['data']['offset']
        assert 3 == page1['data']['limit']
        assert 3 == page1['data']['count']

        status, response = MarvelRequest().get(endpoint, 2, 3)
        page2 = json.loads(response)
        assert 3 == page2['data']['offset']
        assert 3 == page2['data']['limit']
        assert 3 == page2['data']['count']

        status, response = MarvelRequest().get(endpoint, 3, 3)
        page3 = json.loads(response)
        assert 6 == page3['data']['offset']
        assert 3 == page3['data']['limit']
        assert 3 == page3['data']['count']

        pages_ids = [p['id'] for p in pages['data']['results']]
        page1_ids = [p['id'] for p in page1['data']['results']]
        page2_ids = [p['id'] for p in page2['data']['results']]
        page3_ids = [p['id'] for p in page3['data']['results']]

        assert page1_ids == pages_ids[0:3]
        assert page2_ids == pages_ids[3:6]
        assert page3_ids == pages_ids[6:9]

    def test_get_page_not_exist(self):
        endpoint = '/v1/public/characters'
        status, response = MarvelRequest().get(endpoint, 1000, 100)
        assert 200 == status
        data = json.loads(response)
        assert 0 == data['data']['count']
        assert 0 == len(data['data']['results'])
        assert 99900 == data['data']['offset']
        assert 100 == data['data']['limit']

    def test_get_new_etag(self):
        status, response = MarvelRequest().get('/v1/public/characters')
        assert 200 == status
        status, response = MarvelRequest().get('/v1/public/characters')
        assert 304 == status
