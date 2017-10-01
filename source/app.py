from flask import Flask, render_template
import random
from marvel.api import MarvelAPI
from marvel.iterables import StoriesByCharacterIterable, ComicsByCharacterIterable

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    api = MarvelAPI()
    result = api.characters(1009351)

    comics = []
    for s in ComicsByCharacterIterable(1009351):
        comics.append(s)
    comic = random.choice(comics)

    characters = comic['characters']['items']

    data = {
        'name': result[0]['name'],
        'character_image': result[0]['thumbnail']['path'] + '/portrait_incredible.' + result[0]['thumbnail']['extension'],
        'comic': comic,
        'characters': characters
    }
    print(data)
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(port=5001)
