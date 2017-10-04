# The Comics

[![Build Status](https://travis-ci.org/fernandoe/the-comics.svg?branch=master)](https://travis-ci.org/fernandoe/the-comics)
[![Requirements Status](https://requires.io/github/fernandoe/the-comics/requirements.svg?branch=master)](https://requires.io/github/fernandoe/the-comics/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/fernandoe/the-comics/badge.svg?branch=master)](https://coveralls.io/github/fernandoe/the-comics?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://raw.githubusercontent.com/fernandoe/the-comics/master/LICENSE)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/fernandoe)

This is a web service write in Python in order to play with the Marvel API (https://developer.marvel.com) and integrate
third party services that helps on building software.

![Homepage](https://raw.githubusercontent.com/fernandoe/the-comics/docs/sandbox/docs/images/index-page.png)




# Demo

* https://the-comics.herokuapp.com




# External Services

* [Travis](https://travis-ci.org/fernandoe/the-comics): Continuous integration
* [Requires.io](https://requires.io/github/fernandoe/the-comics/requirements/?branch=master): Keep the project secure by monitoring its dependencies
* [Coveralls](https://coveralls.io/github/fernandoe/the-comics?branch=master): Track your code coverage over time
* [Papertrail](https://dashboard.heroku.com/apps/the-comics/resources): Log management (when app is deployed)
* [Heroku Redis](https://dashboard.heroku.com/apps/the-comics/resources): NoSQL database (when app is deployed)




# Installation




## Requirements

* Python 3+
* Redis (for caching)
* Marvel API keys (get yours in https://developer.marvel.com)




## Environment Variables

| Variable | Description | Default Value
| --- | --- | :---:
| `MARVEL_PUBLIC_KEY` | Your Marvel public key | 
| `MARVEL_PRIVATE_KEY` | You marvel private key | 
| `REDIS_URL` | Redis connection string | redis://localhost 
| `TC_ENABLE_CACHE` | Enables the application cache | False




## Quick Start

```
$ pip install pipenv 
$ pipenv --python=python3
$ pipenv install

``` 

### Usage


# Deployment

## Heroku

Add information in how to deploy to heroku




# Contributing

Contributions are welcome! Please feel free to submit a Pull Request.





## Docker

### Redis

```shell
docker run --name marvel-redis \
   -p 6379:6379 \
   -v ~/workspace/docker-volumes/marvel-redis:/data \
   -d redis:3.2.6
```
