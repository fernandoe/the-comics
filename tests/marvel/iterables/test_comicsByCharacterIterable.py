from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import ComicsByCharacterIterable


@patch('marvel.request.r', fakeredis.FakeStrictRedis())
class TestComicsByCharacterIterable(TestCase):
    def test_next(self):
        count = 0
        for _ in ComicsByCharacterIterable(identifier=1009351):
            count = count + 1
        assert count > 0
