#%%
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import time
from datetime import datetime
import json
#%%
class Scraper():

    def __init__(self):
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
        self.ratings = []    

    def get_movie_links(self):
        movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")
        movies = movie_list.find_elements(By.XPATH, "tr/td/a")
        for movie in movies:
            l = movie.get_attribute("href")
            if l not in self.links:
                self.links.append(l)
    
    def get_id(self, mt):
        i = int(mt.rsplit("_", 1)[-1])
        self.get_timestamp()
        self.ids.append(i)

    def get_timestamp(self):
        '''
        change datatype?
        '''
        t = time.time()
        d_t = datetime.fromtimestamp(t)
        s_d_t = d_t.strftime("%d-%m-%Y, %H:%M:%S")
        self.timestamps.append(s_d_t)
        
    def get_movie_title(self):
        t1 = self.driver.find_element(By.XPATH, "//h1[@data-testid = 'hero-title-block__title']").text
        self.titles.append(t1)
        print(self.titles)

    def get_d1(self):
        self.d1 = self.driver.find_element(By.XPATH, "//ul[@data-testid = 'hero-title-block__metadata']")

    def get_movie_release_date(self):
        self.get_d1()
        d2 = int(self.d1.find_element(By.XPATH, "li[1]").text)
        self.release_dates.append(d2)
        print(self.release_dates)

    def get_movie_age_rating(self):
        self.get_d1()
        ar1 = self.d1.find_element(By.XPATH, "li[2]").text
        self.age_ratings.append(ar1)
        print(self.age_ratings)

    def get_movie_runtime(self):
        self.get_d1()
        r1 = self.d1.find_element(By.XPATH, "li[3]").text
        self.runtimes.append(r1)
        print(self.runtimes)

    def get_g1(self):
        self.g1 = self.driver.find_element(By.XPATH, "//div[@class = 'ipc-chip-list__scroller']")

    def get_movie_genre(self):
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
        print(self.genres)

    def get_movie_rating(self):
        mr1 = self.driver.find_element(By.XPATH, "//div[@data-testid = 'hero-rating-bar__aggregate-rating__score']").text
        mr2 = float(mr1.rsplit("/", 1)[0])
        self.ratings.append(mr2)
        print(self.ratings)

    def get_all_movie_textdata(self):
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
            self.data = {
                "id": self.ids, 
                "timestamp": self.timestamps, 
                "title": self.titles, 
                "date": self.release_dates, 
                "age": self.age_ratings, 
                "runtime": self.runtimes,
                "genre": self.genres,
                "ratings": self.ratings
                }
        print(self.data)
        self.download_data()
    
    def download_data(self):
        os.makedirs("raw_data", exist_ok = True)
        with open("raw_data\data.json", "w") as fp:
            json.dump(self.data, fp, indent = 4)

    def download_image(self):
        pass

    def download_image_from_tag(self, image_from_tag):
        pass

    def get_all_movie_imagedata(self):
        pass


if __name__ == "__main__":
    scraper = Scraper()

#%%
scraper.get_all_movie_textdata()
#%%
scraper.driver.quit()
#%%