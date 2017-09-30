from unittest import TestCase

from marvel.iterables import StoriesByCharacterIterable


class TestStoriesByCharacterIterable(TestCase):
    def test_next(self):
        count = 0
        for c in StoriesByCharacterIterable(1009351):
            count = count + 1
            print(c['title'])
        print('count: %s' % count)
