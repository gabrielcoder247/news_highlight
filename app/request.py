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

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(category):
    with urllib.request.urlopen(get_sources_url,data = None) as url:
        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_results)
        '''
        Function that processes the sources result and tranforms them to the list of objects
    
        Args:
        sources_list:A list of sources objects
        returns:
        sources_list:A list of sources objects
        '''

        sources_list = []

        for source_items in sources_results:
            id = sources_items.get('id')
            name = source_items.get('name')
            description = source_item.get('description')
            url = source_item.get('url')
            category = source_item.get('category')
            sources_list.append(source_object)

            
        return sources_list    
                  


