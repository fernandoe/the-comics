from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    return render_template('index.html', context={})

if __name__ == '__main__':
    app.run()