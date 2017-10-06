import os
from unittest import TestCase
from unittest.mock import patch

import fakeredis
import mock

from marvel.request import MarvelRequest

r = fakeredis.FakeStrictRedis()


@patch('marvel.request.r', r)
class TestMarvelRequest(TestCase):
    def setUp(self):
        r.flushall()

    @mock.patch.dict(os.environ, {"TC_ENABLE_CACHE_L1": "True"})
    def test_get_cache_true(self):
        mr = MarvelRequest()
        status_code, response = mr.get('/v1/public/characters/1009351')
        assert 200 == status_code
        status_code, response = mr.get('/v1/public/characters/1009351')
        assert 304 == status_code

    @mock.patch.dict(os.environ, {"TC_ENABLE_CACHE_L1": "False"})
    def test_get_cache_false(self):
        mr = MarvelRequest()
        status_code, response = mr.get('/v1/public/characters/1009351')
        assert 200 == status_code
        status_code, response = mr.get('/v1/public/characters/1009351')
        assert 200 == status_code
