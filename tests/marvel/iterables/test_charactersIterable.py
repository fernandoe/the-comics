from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import CharactersIterable


@patch('marvel.request.r', fakeredis.FakeStrictRedis())
class TestCharactersIterable(TestCase):
    def test_next(self):
        count = 0
        for _ in CharactersIterable():
            count = count + 1
        assert count > 0
