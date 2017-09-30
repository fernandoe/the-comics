from flask import Flask, render_template
import random
from marvel.api import MarvelAPI
from marvel.iterables import StoriesByCharacterIterable

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    api = MarvelAPI()
    result = api.characters(1009351)

    stories = []
    for s in StoriesByCharacterIterable(1009351):
        stories.append(s)
    story = random.choice(stories)

    data = {
        'name': result[0]['name'],
        'character_image': result[0]['thumbnail']['path'] + '/portrait_incredible.' + result[0]['thumbnail']['extension'],
        'story': story
    }
    print(data)
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run()