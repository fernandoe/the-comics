from flask import Flask, render_template

from marvel.api import MarvelAPI

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    api = MarvelAPI()
    result = api.characters(1009351)
    data = {
        'name': result[0]['name']
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run()