import os
from unittest import TestCase
from unittest.mock import patch

import fakeredis
import mock

from marvel.decorator import cached

r = fakeredis.FakeStrictRedis()


class Foo(object):
    @cached
    def method1(self, param1):
        return 'Method1-%s' % param1

    @cached
    def method2(self, param1, param2=1):
        return 'Method2-%s-%s' % (param1, param2)


@patch('marvel.decorator.r', r)
class TestCached(TestCase):
    @mock.patch.dict(os.environ, {"TC_ENABLE_CACHE": "True"})
    def test_method1(self):
        result = Foo().method1(54321)
        assert 'Method1-54321' == result
        assert '"Method1-54321"' == r.get('TC:CACHE:Foo.method1:54321').decode('utf-8')

    @mock.patch.dict(os.environ, {"TC_ENABLE_CACHE": "True"})
    def test_method2(self):
        result = Foo().method2(54321, param2=1)
        assert 'Method2-54321-1' == result
        assert '"Method2-54321-1"' == r.get('TC:CACHE:Foo.method2:54321:param2:1').decode('utf-8')
