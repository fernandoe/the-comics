# The Comics

[![Build Status](https://travis-ci.org/fernandoe/the-comics.svg?branch=master)](https://travis-ci.org/fernandoe/the-comics)
[![Requirements Status](https://requires.io/github/fernandoe/the-comics/requirements.svg?branch=master)](https://requires.io/github/fernandoe/the-comics/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/fernandoe/the-comics/badge.svg?branch=master)](https://coveralls.io/github/fernandoe/the-comics?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://raw.githubusercontent.com/fernandoe/the-comics/master/LICENSE)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/fernandoe)


This is a web service write in Python in order to play with the Marvel API (https://developer.marvel.com) and integrate 
third party services that helps on building software.

The web service starts picking the Hulk as an initial character and choice a random story that he participates. Bellow 
the story choiced, the service shows all characters that are in the story. You can select another one clicking in the 
character picture.


![Homepage](https://raw.githubusercontent.com/fernandoe/the-comics/master/sandbox/docs/images/index-page.png)




# Demo

* https://the-comics.herokuapp.com




# External Services

* [Travis](https://travis-ci.org/fernandoe/the-comics): Continuous integration
* [Requires.io](https://requires.io/github/fernandoe/the-comics/requirements/?branch=master): Keep the project secure by monitoring its dependencies
* [Coveralls](https://coveralls.io/github/fernandoe/the-comics?branch=master): Track your code coverage over time
* [Papertrail](https://dashboard.heroku.com/apps/the-comics/resources): Log management (when app is deployed)
* [Heroku Redis](https://dashboard.heroku.com/apps/the-comics/resources): NoSQL database (when app is deployed)
* [NewRelic](https://newrelic.com) Lets developers, ops, and tech teams measure and monitor the performance of their applications and infrastructure.




# Installation




## Requirements

* Python 3+
* Redis (for caching)
* Marvel API keys (get yours in https://developer.marvel.com)




## Environment Variables

| Variable | Description | Default Value
| --- | --- | :---:
| `MARVEL_PUBLIC_KEY` | Your Marvel public key | 
| `MARVEL_PRIVATE_KEY` | You Marvel private key | 
| `REDIS_URL` | Redis connection string | redis://localhost 
| `TC_ENABLE_CACHE_L1` | Enables the Marvel API cache (etag) | False
| `TC_ENABLE_CACHE_L2` | Enables the application cache | False
| `TC_LIMIT_PAGES` | Limits the number of pages returned in searches | 






## Installing and Running


### Redis


You will need Redis installed and running in order to play with the application. You can install it using:




#### Install locally

 
* Instructinos: https://redis.io/download




#### Using Docker


```shell
docker run --name marvel-redis \
   -p 6379:6379 \
   -v ~/workspace/docker-volumes/marvel-redis:/data \
   -d redis:3.2.6
```



### Steps to Install and Running Locally

```shell
$ git clone https://github.com/fernandoe/the-comics
$ cd the-comics
$ virtualenv .venv --python=python3
$ source .venv/bin/activate
$ pip install -r requirements/development.txt
$ export FLASK_DEBUG=1 
$ export MARVEL_PRIVATE_KEY=[your private key]
$ export MARVEL_PUBLIC_KEY=[your public key] 
$ export PYTHONPATH=src
$ export TC_ENABLE_CACHE_L1=True
$ export TC_ENABLE_CACHE_L2=True
$ export TC_LIMIT_PAGES=3
$ python src/app.py
``` 




## Steps to Install and Running on Heroku


```shell
$ git clone https://github.com/fernandoe/the-comics
$ cd the-comics
$ heroku create
$ heroku config:set MARVEL_PRIVATE_KEY=[your private key]
$ heroku config:set MARVEL_PUBLIC_KEY=[your public key]
$ heroku config:set PYTHONPATH=src
$ heroku config:set TC_ENABLE_CACHE_L1=True
$ heroku config:set TC_ENABLE_CACHE_L2=True
$ heroku config:set TC_LIMIT_PAGES=3
$ heroku addons:create papertrail
$ heroku addons:create heroku-redis:hobby-dev
$ heroku addons:create newrelic:wayne  # Install NewRelic
$ heroku config:set NEW_RELIC_APP_NAME='The Comics'  # NewRelic configuration
$ git push heroku master
$ heroku open
``` 




# Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
