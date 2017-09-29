from unittest import TestCase

from source.marvel.api import MarvelAPI


class TestMarvelAPI(TestCase):
    def test_characters(self):
        r = MarvelAPI().characters()
        assert r.status_code == 200

    def test_characters_hulk(self):
        r = MarvelAPI().characters(1009351)
        assert r.status_code == 200

    def test_comics(self):
        r = MarvelAPI().comics()
        print(r)
        assert r.status_code == 200

    def test_stories_by_character(self):
        r = MarvelAPI().stories_by_character(1009351)
        assert r.status_code == 200
