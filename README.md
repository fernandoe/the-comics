# the-comics

[![Build Status](https://travis-ci.org/fernandoe/the-comics.svg?branch=master)](https://travis-ci.org/fernandoe/the-comics)
[![Requirements Status](https://requires.io/github/fernandoe/the-comics/requirements.svg?branch=master)](https://requires.io/github/fernandoe/the-comics/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/fernandoe/the-comics/badge.svg?branch=master)](https://coveralls.io/github/fernandoe/the-comics?branch=master)

Example app for testing the Marvel API


## Docker

### Redis

```shell
docker run --name marvel-redis \
   -p 6379:6379 \
   -v ~/workspace/docker-volumes/marvel-redis:/data \
   -d redis:3.2.6
```
