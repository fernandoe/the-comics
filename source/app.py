import random

from flask import Flask, render_template

from marvel.api import MarvelAPI
from marvel.iterables import ComicsByCharacterIterable
from marvel.request import MarvelRequest

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    # api = MarvelAPI()
    # result = api.characters(1009351)

    # comics = []
    # for s in ComicsByCharacterIterable(1009351):
    #     comics.append(s)
    # comic = random.choice(comics)

    # characters = comic['characters']['items']

    # data = {
    #     'name': result[0]['name'],
    #     'character_image': result[0]['thumbnail']['path'] + '/portrait_incredible.' + result[0]['thumbnail']['extension'],
    #     'comic': comic,
    #     'characters': characters
    # }

    character = MarvelRequest().characters(identifier=1009351)
    character_name = character['name']
    character_image = character['thumbnail']['path'] + '/standard_large.' + character['thumbnail']['extension']

    comics = []
    for s in ComicsByCharacterIterable(1009351):
        comics.append(s)
    comic = random.choice(comics)
    comic_title = comic['title']
    comic_description = comic['description']
    comic_image = comic['thumbnail']['path'] + '/portrait_incredible.' + comic['thumbnail']['extension']

    data = {
        'character_name': character_name,
        'character_image': character_image,
        'comic_title': comic_title,
        'comic_description': comic_description,
        'comic_image': comic_image,
        'characters': 'characters'
    }

    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(port=5001)
