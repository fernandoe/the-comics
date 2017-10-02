from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import StoriesByCharacterIterable


class TestStoriesByCharacterIterable(TestCase):
    @patch('marvel.request.r', fakeredis.FakeStrictRedis())
    def test_next(self):
        count = 0
        for c in StoriesByCharacterIterable(1009351):
            count = count + 1
            print(c['title'])
        print('count: %s' % count)
