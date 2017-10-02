from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import StoriesByCharacterIterable


@patch('marvel.request.r', fakeredis.FakeStrictRedis())
class TestStoriesByCharacterIterable(TestCase):
    def test_next(self):
        count = 0
        for _ in StoriesByCharacterIterable(identifier=1009351):
            count = count + 1
        assert count == 101
