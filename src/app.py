import logging
import random
from logging.config import dictConfig

from flask import Flask, render_template, request

from marvel.iterables import ComicsByCharacterIterable, CharacteresByComicIterable
from marvel.request import MarvelRequest

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s] [%(process)d] [%(thread)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'marvel': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
})

log = logging.getLogger('marvel')
app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    identifier = request.args.get('identifier', None)
    if identifier is None:
        identifier = 1009351  # Hulk
    log.info('Requesting CharacterID={CharacterID}'.format(CharacterID=identifier))

    character = MarvelRequest().characters(identifier=identifier)
    character_name = character['name']
    character_image = character['thumbnail']['path'] + '/standard_large.' + character['thumbnail']['extension']
    log.info('CharacterName={CharacterName}'.format(CharacterName=character_name))

    comics = []
    for s in ComicsByCharacterIterable(identifier=identifier):
        comics.append(s)
    comic = random.choice(comics)
    log.info('Selected ComicID={ComicID}'.format(ComicID=comic['id']))

    comic_title = comic['title']
    comic_description = comic['description']
    comic_image = comic['thumbnail']['path'] + '/portrait_incredible.' + comic['thumbnail']['extension']

    characters = []
    for c in CharacteresByComicIterable(identifier=comic['id']):
        characters.append(c)
    data = {
        'character_name': character_name,
        'character_image': character_image,
        'comic_title': comic_title,
        'comic_description': comic_description,
        'comic_image': comic_image,
        'characters': characters
    }

    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run()
