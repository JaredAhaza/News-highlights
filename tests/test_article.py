import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    """
    Test Class to test the behaviours we expect in our applications
    """

    def setUp(self):
        """
        This will function runs before every Test. Its a
        built in unittest function that allows us to test our object.
        """
        self.new_articles = Articles(1234,'bbc news','bbc news','A Harrowing experience','A story of a man saved from drowning','http://www.bbc.co.uk/news/world-asia-42849060','https://ichef-1.bbci.co.uk/news/1024/branded_news/117AD/production/_99779517_dinghy.jpg','2018-01-28T04:37:59')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles))


