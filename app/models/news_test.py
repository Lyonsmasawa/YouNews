import unittest
from models import news

class NewsTest(unittest.TestCase):
    """
    Test class to test behaviour of class
    """
    def setUp(self):
        """
        run before every test
        """
        self.new_news = News(1234, "News", "This is news", "https://newslink.com", "category", "En" )
