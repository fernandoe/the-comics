import json
import logging
import os

import redis

log = logging.getLogger('marvel')
r = redis.from_url(os.environ.get("REDIS_URL", 'redis://localhost'))


def cached(method):
    def decorated(*args, **kwargs):
        if not os.environ.get("TC_ENABLE_CACHE_L2", False):
            return method(*args, **kwargs)
        key = build_key(method, args, kwargs)
        response = r.get(key)
        if response is None:
            response = method(*args, **kwargs)
            r.set(key, json.dumps(response))
        else:
            log.debug('[CACHE L2] Retrieve from cache. Key=%s' % key)
            response = json.loads(response)
        return response

    return decorated


def build_key(method, args, kwargs):
    result = 'TC:CACHE:%s' % method.__qualname__
    for key in args[1:]:
        result = '%s:%s' % (result, key)
    for key in sorted(kwargs):
        result = '%s:%s:%s' % (result, key, kwargs[key])
    return result
