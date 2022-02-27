from flask import render_template
from app import app
from app.requests import get_news

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

@app.route('/source/<source_id>')
def articles(source_id):
    """dislays articles from a given source"""
    return render_template("articles.html", id = source_id)