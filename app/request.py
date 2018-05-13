import urllib
import json
from .models import Source
from .models import Articles


#Getting api key
api_key = None

#Getting base url
base_url = None

#Getting source_url
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEW_URL']
    source_url = app.config['SOURCE_NEWS_URL']

def get_sources(country, category):
    '''
    Function that gets json response to our url request
    '''
    get_news_url = base_url.format(country, category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data.decode('utf'))

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['source']
            source_results = process_sources(source_results_list)
        
        return source_results

def process_sources(source_list):
    '''
    Function processing the dictionary and outputs a list of objects
    '''
    news_results = []
    for source in  source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            source_object = Source(id,name,description,url,category,country)
            news_results.append(source_object)


    return news_results

def get_articles(id):
    '''
    Function that gets json response to our url request
    '''
    get_source_news_url = source_url.format(id,api_key)
    with urllib.request.urlopen(get_source_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data.decode('utf'))

        news_results = None

    if get_news_response['articles']:
        news_results_list = get_news_response['articles']
        news_results = process_articles(news_results_list)

    return news_results

def process_articles(articles_list):
    '''
    Function processing the dictionary and outputs a list of objects
    '''
    news_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        publishedAt = result.get('publishedAt')

        if url:
            source_object = Articles(id,name,author,title,description,url,publishedAt)
            news_results.append(source_object)

        return news_results