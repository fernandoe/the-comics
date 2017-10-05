import os
from unittest import TestCase
from unittest.mock import patch

import fakeredis
import mock

from marvel.iterables import CharactersIterable


@patch('marvel.request.r', fakeredis.FakeStrictRedis())
class TestCharactersIterable(TestCase):
    @mock.patch.dict(os.environ, {'TC_LIMIT_PAGES': '2'})
    def test_next(self):
        count = 0
        for _ in CharactersIterable():
            count = count + 1
        assert count == 101
