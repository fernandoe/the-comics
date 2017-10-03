import random

from flask import Flask, render_template, request

from marvel.iterables import ComicsByCharacterIterable, CharacteresByComicIterable
from marvel.request import MarvelRequest

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    identifier = request.args.get('identifier', None)
    if identifier is None:
        identifier = 1009351  # Hulk
    character = MarvelRequest().characters(identifier=identifier)
    character_name = character['name']
    character_image = character['thumbnail']['path'] + '/standard_large.' + character['thumbnail']['extension']

    comics = []
    for s in ComicsByCharacterIterable(identifier=identifier):
        comics.append(s)
    comic = random.choice(comics)
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
    app.run(port=5001)
