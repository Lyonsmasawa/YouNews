from flask import render_template
from app import app
from app.requests import get_news, get_articles

@app.route('/')
def index():
    """
    Root page
    """

    #show all the news sources
    all_news = get_news()
    print("Available sources")
    title = "YouNews"
    return render_template('index.html', title = title, all_news = all_news)

@app.route('/source/<id>')
def articles(id):
    """dislays articles from a given source"""

    articles = get_articles(id)
    title = f'{id}'

    return render_template("articles.html", id = id, title = title, articles = articles)

@app.errorhandler(404)
def four_Ow_four(error):
    """
    Function to render the 404 error
    """
    return render_template('fourOwfour.html'),404
