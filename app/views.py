from flask import render_template
from app import app

@app.route('/')
def index():
    """
    Root page
    """
    title = "YouNews"
    return render_template('index.html', title = title)

@app.route('/source/<int:source_id>')
def articles(source_id):
    """dislays articles from a given source"""
    return render_template("articles.html", id = source_id)