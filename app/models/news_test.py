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
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        """"
        Test initialization
        """
        self.assertEqual(self.new_news.id, 1234)
        self.assertEqual(self.new_news.name, "News")
        self.assertEqual(self.new_news.description, "This is news")
        self.assertEqual(self.new_news.url, "https://newslink.com")
        self.assertEqual(self.new_news.category, "category")
        self.assertEqual(self.new_news.language, "En")

if  __name__ == '__main__':
    unittest.main()
