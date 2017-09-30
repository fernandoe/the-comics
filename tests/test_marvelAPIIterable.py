from unittest import TestCase

from marvel.api import MarvelAPIIterable, Counter


class TestMarvelAPIIterable(TestCase):
    def test_next(self):
        # print('iniciando')
        # for i in MarvelAPIIterable(['1', '2']):
        #     print('dentro do FOR')
        #     print(i)
        # print('Done')

        # for char in MarvelAPIIterable(['1', '2']):
        #     print(char)

        for i in Counter(5, 10):
            print(i)
