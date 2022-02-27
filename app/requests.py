from app import app
import urllib.request, json
from .models import news

New = news.New


#get API key
api_key = app.config['NEWS_API_KEY']

#get URL 
base_url = app.config['NEWS_BASE_URL']

def get_news():
    """
    Gets the JSON response to our URL request
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read
        get_movies_response = json.loads(get_news_data)

        news_results = None 

        if get_movies_response['results']:
            news_results_list = get_movies_response['results']
            movie_results = process_results(news_results_list)

    return movie_results