import json
from app import app

#get API key
api_key = app.config['NEWS_API_KEY']
import urllib.request, json
from .models import news

New = news.New

