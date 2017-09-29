from unittest import TestCase

from source.marvel.api import MarvelAPI


class TestMarvelAPI(TestCase):
    def test_characters(self):
        r = MarvelAPI().characters()
        print(r)
        print(MarvelAPI().characters())
        assert r.status_code == 200

    def test_characters_hulk(self):
        r = MarvelAPI().characters(1009351)
        assert r.status_code == 200
        # print(MarvelAPI().characters())

    def test_comics(self):
        r = MarvelAPI().comics()
        print(r)
        self.assertEqual(200, r.status_code)
        assert r.status_code == 200
