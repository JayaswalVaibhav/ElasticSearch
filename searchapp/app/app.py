from flask import Flask, render_template, request
from es import search_movie

app = Flask(__name__)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        movie = request.form["movie"]
        hits = search_movie(movie)

        return render_template('search.html', data=hits)
    return render_template('search.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

