# %%
import scraper
import unittest
import json
import requests
import random

class TestScraper(unittest.TestCase):

        def setUp(self):
                self.Scraper = scraper.Scraper()
                self.url = "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=CY8VXWHRR7M7P2XA1Q55&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"

        @unittest.skip
        def test_1_get_movie_links(self):
                self.Scraper.get_movie_links()
                self.assertIsInstance(self.Scraper.links, list) 
                self.assertIsInstance(self.Scraper.links[0], str)
                print("get_movie_links returns a list of links")    
                print(self.Scraper.links[0]) 
                
        @unittest.skip        
        def test_2_get_id(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_id(self.url)
                self.assertIsInstance(self.Scraper.ids[0], int)
                print ("get_id returns a list of integers")
                print(self.Scraper.id)
        
        @unittest.skip  
        def test_3_get_timestamp(self):
                self.Scraper.get_timestamp()
                self.assertEqual(len(self.Scraper.timestamps[0]), 19)
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
                self.Scraper.get_release_age_runtime_xpath()
                self.Scraper.get_movie_release_date()
                self.assertEqual(len(str(self.Scraper.release_dates[0])), 4)
                self.assertIsInstance(self.Scraper.release_dates[0], int)
                print ("release_date is 4 characters long and an integer")
                print(self.Scraper.release_dates[0])

        @unittest.skip         
        def test_7_get_movie_age_rating(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_release_age_runtime_xpath()
                self.Scraper.get_movie_age_rating()
                self.assertLessEqual(len(self.Scraper.age_ratings[0]), 4)
                self.assertIsInstance(self.Scraper.age_ratings[0], str)
                print("age_rating is less than or equal to 4 characters and is a string")
                print(self.Scraper.ratings[0])

        @unittest.skip         
        def test_8_get_movie_runtime(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_release_age_runtime_xpath()
                self.Scraper.get_movie_runtime()
                self.assertLessEqual(len(self.Scraper.runtimes[0]), 6)
                self.assertIsInstance(self.Scraper.runtimes[0], str)
                print("runtime is less than or equal to 6 characters and is a string")
                print(self.Scraper.runtimes[0])

        @unittest.skip         
        def test_9_get_movie_genre(self):
                self.Scraper.driver.get(self.url)
                self.Scraper.get_movie_genre()
                self.assertLessEqual(len(self.Scraper.genres[0].rsplit("/", 2)), 3)
                self.assertIsInstance(self.Scraper.genres[0], str)
                print("genre is less than equal to 3 characters and is a string")
                print(self.Scraper.genres[0])

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
                

        #@unittest.skip    
        def test_12_download_image_data(self):
                self.image_data = requests.get("https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL75_UX190_CR0,0,190,281_.jpg").content
                self.image_name = "06122022_203302_1"
                self.Scraper.download_image_data()
                
                

        @unittest.skip         
        def test_13_download_text_data(self):
                self.Scraper.data = {
                "id": 1, 
                "timestamp": "03-12-2022_00:23:56", 
                "title": "The Shawshank Redemption", 
                "date": 1994, 
                "age": "15", 
                "runtime": "2h 22m",
                "genre": "Drama",
                "rating": 9.3,
                "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL75_UX190_CR0,0,190,281_.jpg"
                }
                self.Scraper.download_text_data()
                with open("raw_data/data.json", "r") as fp:
                        json_object = json.load(fp)
                self.assertEqual(self.Scraper.data, json_object)
                self.assertEqual(len(json_object), 9)
                print("data is downloaded to a json file as a dictionary with 9 elements")
                print(json_object)



        @unittest.skip         
        def test_14_get_all_movie_data(self):
                
                no_of_movies = 5
                self.Scraper.get_all_movie_data(no_of_movies)
                index = random.randint(0, no_of_movies - 1)
                self.assertIsInstance(self.Scraper.links, list)
                self.assertIsInstance(self.Scraper.links[index], str)
                self.assertIsInstance(self.Scraper.ids[index], int)
                self.assertEqual(len(self.Scraper.timestamps[index]), 19)
                self.assertIsInstance(self.Scraper.titles[index], str)


                self.assertEqual(len(str(self.Scraper.release_dates[index])), 4)
                self.assertIsInstance(self.Scraper.release_dates[index], int)
                self.assertLessEqual(len(self.Scraper.age_ratings[index]), 4)
                self.assertIsInstance(self.Scraper.age_ratings[index], str)
                self.assertLessEqual(len(self.Scraper.runtimes[index]), 6)
                self.assertIsInstance(self.Scraper.runtimes[index], str)
                self.assertLessEqual(len(self.Scraper.genres[index].rsplit("/", 2)), 3)
                self.assertIsInstance(self.Scraper.genres[index], str)
                self.assertIsInstance(self.Scraper.ratings[index], float)
                self.assertEqual(self.Scraper.images[index][-4:], ".jpg")


                with open("raw_data/data.json", "r") as fp:
                        json_object = json.load(fp)
                self.assertEqual(self.Scraper.data, json_object)
                self.assertEqual(len(json_object), 9)
                self.assertIsInstance(self.Scraper.data, dict)
                print("get_all_movie_data returns data, a dictionary")


        def tearDown(self):
                self.Scraper.exit()

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)

# %%
