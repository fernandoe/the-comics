from unittest import TestCase
from unittest.mock import patch

import fakeredis

from marvel.iterables import CharactersIterable


class TestCharactersIterable(TestCase):
    @patch('marvel.request.r', fakeredis.FakeStrictRedis())
    def test_next(self):
        count = 0
        for c in CharactersIterable():
            count = count + 1
            print(c['name'])
        print('count: %s' % count)
