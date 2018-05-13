from flask import render_template
from . import main
from ..request import get_sources, get_articles

@main.route('/')
def index():
    '''
    function displaying index
    '''
    general_list = get_sources('us', 'general')
    business_list = get_sources('us', 'business')
    technology_list = get_sources('us', 'technology')
    sports_list = get_sources('us', 'sports')
    health_list = get_sources('us', 'health')
    science_list = get_sources('us', 'science')
    entertainment_list = get_sources('us', 'entertainment')
    return render_template('index.html',general=general_list,business=business_list,technology=technology_list,sports=sports_list,health=health_list,science=science_list,entertainment=entertainment_list)


@main.route('/news/<id>')
def news(id):
    '''
    Function that returns articles page from a highlight
    '''
    news_args = get_articles(id)
    highlight_args = 'Route working'

    return render_template('news.html',highlight_param=highlight_args,news=news_args)
