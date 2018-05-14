import os

class Config:
    '''
    General configuration class
    '''

    BASE_NEWS_API_URL= 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   


class ProdConfig(Config):
    '''
    Productions configurations child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings

    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}