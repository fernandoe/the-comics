import os
from unittest import TestCase

import mock

from marvel.iterables import BaseIterable


class FooIterable(BaseIterable):
    def __init__(self):
        self.total_pages = 20
        super(FooIterable, self).__init__()

    def get_items(self):
        if self.total_pages == 0:
            raise StopIteration
        else:
            self.total_pages = self.total_pages - 1
            return [self.total_pages]


class TestBaseIterable(TestCase):
    def test_limit_pages_not_defined(self):
        count = 0
        for _ in FooIterable():
            count = count + 1
        assert count == 20

    @mock.patch.dict(os.environ, {'TC_LIMIT_PAGES': '3'})
    def test_limit_pages_with_3(self):
        count = 0
        for _ in FooIterable():
            count = count + 1
        assert count == 3
