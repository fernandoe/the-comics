from unittest import TestCase

from marvel.iterables import CharactersIterable


class TestCharactersIterable(TestCase):
    def test_next(self):
        count = 0
        for c in CharactersIterable():
            count = count + 1
            print(c['name'])
        print('count: %s' % count)
