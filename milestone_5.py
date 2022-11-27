#%%
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import time
from datetime import datetime
import json
import requests
#%%
class Scraper():
    '''
    A top movie list data scraper that scrapes all the useful data for the top 250 movies from the IMDB website.

    Attributes:
    ----------
    links: list
        A list of links for each movie.
    ids: list
        A list of ids associated with each top movie.
    timestamps: list
        A list of timestamps of when each movie page is scraped.
    titles: list
        A list of titles for each movie.
    release_dates: list
        A list of release dates for each movie.
    age_ratings: list
        A list of age ratings for each movie.
    runtimes: list
        A list of runtimes for each movie.
    genres: list
        A list of genres for each movie.    
    ratings: list
        A list of ratings for each movie.
    images:list
        A list of images for each movie.
    Methods:
    -------
    get_movie_links
        Scrapes website for all top movie links.
    get_id
        Uses top movie link to generate unique ids for each data entry.
    get_timestamp
        Generates timestamp for when the data for each movie is scraped in the form of d-m-Y_H:M:S.
    get_movie_title
        Scrapes movie title.
    get_d1
        Scrapes for xpath of the block containing movie release date, rating and runtime.
    get_movie_release_date
        Scrapes movie release date.
    get_movie_age_rating
        Scrapes movie age rating.
    get_movie_runtime
        Scrapes movie runtime.
    get_g1
        Scrapes for xpath of the movie genre.
    get_movie_genre
        Scrapes movie genre.
    get_movie_rating 
        Scrapes movie rating.
    get_movie_image
        Scrapes movie image source link.
    download_image_data
        Downloads image locally to an images folder as a jpeg file.
    download_text_data
        Downloads data dictionaries locally to a raw_data folder as a json file.
    get_all_movie_text_data
    '''
    def __init__(self):
        '''
        Constructs all the neccessary attributes for the scraper object. 
        Loads the IMDB top 250 movie site using Selenium.
        '''

        self.driver = webdriver.Chrome()
        url = "https://www.imdb.com/chart/top"
        self.driver.get(url)
        time.sleep(2)
        
        self.links = []
        self.ids = []
        self.timestamps = []
        self.titles = []
        self.release_dates = []
        self.age_ratings = []
        self.runtimes = []
        self.genres = []
        self.images = []   

    def get_movie_links(self):
        '''
        
        '''
        movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")
        movies = movie_list.find_elements(By.XPATH, "tr/td/a")
        for movie in movies:
            l = movie.get_attribute("href")
            if l not in self.links:
                self.links.append(l)
    
    def get_id(self, mt):
        '''
        
        '''
        self.i = int(mt.rsplit("_", 1)[-1])
        self.get_timestamp()
        self.ids.append(self.i)

    def get_timestamp(self):
        '''
        change datatype?
        '''
        t = time.time()
        d_t = datetime.fromtimestamp(t)
        self.s_d_t = d_t.strftime("%d-%m-%Y_%H:%M:%S")
        self.timestamps.append(self.s_d_t)
        
    def get_movie_title(self):
        '''
        
        '''
        t1 = self.driver.find_element(By.XPATH, "//h1[@data-testid = 'hero-title-block__title']").text
        self.titles.append(t1)

    def get_d1(self):
        '''
        
        '''
        self.d1 = self.driver.find_element(By.XPATH, "//ul[@data-testid = 'hero-title-block__metadata']")

    def get_movie_release_date(self):
        '''
        
        '''
        self.get_d1()
        d2 = int(self.d1.find_element(By.XPATH, "li[1]").text)
        self.release_dates.append(d2)

    def get_movie_age_rating(self):
        '''
        
        '''
        self.get_d1()
        ar1 = self.d1.find_element(By.XPATH, "li[2]").text
        self.age_ratings.append(ar1)

    def get_movie_runtime(self):
        '''
        
        '''
        self.get_d1()
        r1 = self.d1.find_element(By.XPATH, "li[3]").text
        self.runtimes.append(r1)

    def get_g1(self):
        '''
        
        '''
        self.g1 = self.driver.find_element(By.XPATH, "//div[@class = 'ipc-chip-list__scroller']")

    def get_movie_genre(self):
        '''
        
        '''
        g1 = self.driver.find_element(By.XPATH, "//div[@class = 'ipc-chip-list__scroller']")
        try:
            g2 = g1.find_element(By.XPATH, "a[1]").text
            g3 = g1.find_element(By.XPATH, "a[2]").text
            g4 = g1.find_element(By.XPATH, "a[3]").text
            g5 = [g2, g3, g4]
            g6 = "/".join(g5)
        except:
            try:
                g2 = g1.find_element(By.XPATH, "a[1]").text
                g3 = g1.find_element(By.XPATH, "a[2]").text
                g5 = [g2, g3]
                g6 = "/".join(g5)
            except:
                g2 = g1.find_element(By.XPATH, "a[1]").text
                g5 = [g2]
                g6 = "/".join(g5)
        self.genres.append(g6)
        
    def get_movie_rating(self):
        '''
        
        '''
        mr1 = self.driver.find_element(By.XPATH, "//div[@data-testid = 'hero-rating-bar__aggregate-rating__score']").text
        mr2 = float(mr1.rsplit("/", 1)[0])
        self.ratings.append(mr2)

    def get_movie_image(self):
        '''
        
        '''
        i1 = self.driver.find_element(By.XPATH, "//img")
        i2 = i1.get_attribute("src")
        self.images.append(i2)
        return i2
        
    def download_image_data(self, mt):
        '''
        
        '''
        os.makedirs("raw_data/images", exist_ok = True)
        img_url = self.get_movie_image()
        img_data = requests.get(img_url).content
        img_datetime = self.s_d_t.replace("-", "").replace(":", "")
        img_id = str(self.i)
        img_name = img_datetime + "_" + img_id
        with open(f"raw_data/images/{img_name}.jpg", 'wb') as handler:
            handler.write(img_data)

    def download_text_data(self):
        '''
        
        '''
        os.makedirs("raw_data", exist_ok = True)
        with open("raw_data/data.json", "w") as fp:
            json.dump(self.data, fp, indent = 4)

    def get_all_movie_textdata(self):
        '''
        
        '''
        self.get_movie_links()
        for mt in self.links[:5]:
            self.driver.get(mt)
            self.get_id(mt)
            self.get_movie_title()   
            self.get_movie_release_date()
            self.get_movie_age_rating()
            self.get_movie_runtime()
            self.get_movie_genre()
            self.get_movie_rating()
            self.download_image_data(mt)
            self.data = {
                "id": self.ids, 
                "timestamp": self.timestamps, 
                "title": self.titles, 
                "date": self.release_dates, 
                "age": self.age_ratings, 
                "runtime": self.runtimes,
                "genre": self.genres,
                "rating": self.ratings,
                "image": self.images
                }
            self.download_text_data()
        print(self.data)

if __name__ == "__main__":
    scraper = Scraper()
#%%
scraper.get_all_movie_textdata()
#%%
scraper.driver.quit()