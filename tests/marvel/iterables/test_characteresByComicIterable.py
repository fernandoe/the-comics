from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import CharacteresByComicIterable


@patch('marvel.request.r', fakeredis.FakeStrictRedis())
class TestCharacteresByComicIterable(TestCase):
    def test_next(self):
        count = 0
        for _ in CharacteresByComicIterable(identifier=27649):
            count = count + 1
        assert count > 0
