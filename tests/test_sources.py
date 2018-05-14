import unittest
from app.models import Source
# Source = news_source.Source


class NewsSource(unittest.TestCase):
    """
    Test Class to test the behaviours we expect in our applications
    """

    def setUp(self):
        """
        This will function runs before every Test. Its a
        built in unittest function that allows us to test our object.
        """

        self.new_source = Source(1234,'Harrowing experience','Article of a man saved from drowning','http://www.bbc.co.uk/news/world-asia-42849060','general','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
