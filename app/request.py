import urllib
import json
from .models import Source
from .models import Articles


#Getting api key
api_key = None

#Getting base url
base_url = None

Getting source_url
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = 
    source_url =
