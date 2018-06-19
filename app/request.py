import urllib.request,json
from .models import Source,Article

#Getting Api key

api_key = None
#Getting the base urls
source_base_url = None
article_base_url = None

def configure_request(app):
    '''
    Function to acquire  the api key and base urls
    '''
    global api_key,source_base_url,article_base_url
    api_key = app.config['NEWS_SOURCES_BASE_URL']
    source_base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']