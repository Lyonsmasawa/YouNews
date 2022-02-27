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
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None 

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    processes the results list and transforms them to a list of objects
    """
    news_results = []
    for item in news_list:
        id = item.get("id")
        name = item.get("name")
        description = item.get("description")
        url = item.get("url")
        category = item.get("category")
        language = item.get("language")
        country = item.get("country")
    
        news_object = New(id, name, description, url, category, language, country)
        news_results.append(news_object)

    return news_results