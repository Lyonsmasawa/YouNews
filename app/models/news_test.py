import unittest
import news

News = news.New

class NewsTest(unittest.TestCase):
    """
    Test class to test behaviour of class
    """
    def setUp(self):
        """
        run before every test
        """
        self.new_news = News(1234, "News", "This is news", "https://newslink.com", "category", "En" )
    
    def test_instance(self):
        """Test instance"""
        self.assertTrue(isinstance(self.new_news, New))

if  __name__ == '__main__':
    unittest.main()
