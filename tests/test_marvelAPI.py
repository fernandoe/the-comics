from unittest import TestCase

from source.marvel.api import MarvelAPI


class TestMarvelAPI(TestCase):
    def test_characters(self):
        print(MarvelAPI().characters())
