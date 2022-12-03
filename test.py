#%%

import unittest

class TestScraper(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
        
if __name__ == "__main__":
    unittest.main()

# %%

#%%
def tearDown(self):
        self.Scraper.driver.exit()

def test_1_get_movie_links(self):
        self.Scraper.get_movie_links()
        self.assertIsInstance(self.Scraper.links, list)
        print("get_movie_links returns a list variable")     

def setUp(self):
        self.Scraper = scraper.Scraper()