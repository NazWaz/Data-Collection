# %%
import scraper
import unittest

class TestScraper(unittest.TestCase):

        def setUp(self):
                self.Scraper = scraper.Scraper()
                self.url = "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=CY8VXWHRR7M7P2XA1Q55&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"

        @unittest.skip
        def test_1_get_movie_links(self):
                self.Scraper.get_movie_links()
                self.assertIsInstance(self.Scraper.links, list)
                print("get_movie_links returns a list variable")    
                print(self.Scraper.links[0]) 
                
        @unittest.skip        
        def test_2_get_id(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_id(self.url)
                self.assertIsInstance(self.Scraper.id, int)
                print ("get_id returns an integer variable")
                print(self.Scraper.id)
        
        @unittest.skip  
        def test_3_get_timestamp(self):
                self.Scraper.get_timestamp()
                self.assertEqual(len(self.Scraper.datetime), 19)
                print ("datetime is 19 characters long")
                print(self.Scraper.datetime)

        @unittest.skip  
        def test_4_get_movie_title(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_title()
                self.assertIsInstance(self.Scraper.titles[0], str)
                print ("get_movie_title returns a list of strings")
                print(self.Scraper.titles[0])

        @unittest.skip  
        def test_5_get_release_age_runtime_xpath(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_release_age_runtime_xpath()
                '''
                fix test
                '''
        @unittest.skip 
        def test_6_get_movie_release_data(self):
                self.Scraper.driver.get(self.url)
                
                self.Scraper.get_movie_release_date()
                self.assertEqual(len(self.Scraper.release_dates[0]), 4)
                self.assertIsInstance(self.Scraper.release_dates[0], int)
                print ("release_date is 4 characters long and an integer")
                print(self.Scraper.release_dates[0])

        @unittest.skip         
        def test_7_get_movie_age_rating(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_age_rating()

        @unittest.skip         
        def test_8_get_movie_runtime(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_runtime()

        @unittest.skip         
        def test_9_get_movie_genre(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_genre()

        @unittest.skip       
        def test_10_get_movie_rating(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_rating()
                self.assertIsInstance(self.Scraper.ratings[0], float)
                print ("get_movie_rating returns a list of floats")
                print(self.Scraper.ratings[0])

        @unittest.skip  
        def test_11_get_movie_image(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_image()
                self.assertEqual(self.Scraper.images[0][-4:], ".jpg")
                print ("get_movie_image returns a list of links ending in jpg")
                print(self.Scraper.images[0])
                

        @unittest.skip         
        def test_12_download_image_data(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.download_image_data()

        @unittest.skip         
        def test_13_download_text_data(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.download_text_data()

        @unittest.skip         
        def test_14_get_all_movie_data(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_all_movie_data()

        def tearDown(self):
                self.Scraper.exit()

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)

# %%
def test_2_get_id(self):
                self.Scraper.get_movie_links()
                movie_link = self.Scraper.links[0]
                self.Scraper.driver.get(movie_link)
                self.Scraper.get_id(movie_link)
                self.assertIsInstance(self.Scraper.id, int)
                print ("get_id returns an integer variable")