from unittest import TestCase

from marvel.api import MarvelAPIIterable


class TestMarvelAPIIterable(TestCase):
    def test_next(self):
        # print('iniciando')
        # for i in MarvelAPIIterable(['1', '2']):
        #     print('dentro do FOR')
        #     print(i)
        # print('Done')

        for char in MarvelAPIIterable():
            print(char)