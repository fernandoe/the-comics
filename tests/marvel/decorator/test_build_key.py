from unittest import TestCase

from marvel.decorator import build_key


class TestBuildKey(TestCase):
    def test_build_key(self):
        key = build_key(self.test_build_key, (self, 'first',), {'1': 'a', '3': 'c', '2': 'b'})
        assert 'TC:CACHE:TestBuildKey.test_build_key:first:1:a:2:b:3:c' == key
