#%%
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import time
#%%
class Scraper():

    def __init__(self):
        self.driver = webdriver.Chrome()
        url = "https://www.imdb.com/chart/top"
        self.driver.get(url)
        time.sleep(2)
        

        self.links = []
        self.titles = []
        self.release_dates = []
        self.age_ratings = []
        self.runtimes = []
        self.genres = []
        self.ratings = []    
        self.reviews = []

    def get_movie_links(self):
        movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")
        movies = movie_list.find_elements(By.XPATH, "tr/td/a")
        for movie in movies:
            l = movie.get_attribute("href")
            if l not in self.links:
                self.links.append(l)

    def get_movie_title(self):
        t1 = self.driver.find_element(By.XPATH, "//h1[@data-testid='hero-title-block__title']").text
        self.titles.append(t1)
        print(self.titles)

    def get_d1(self):
        self.d1 = self.driver.find_element(By.XPATH, "//ul[@data-testid='hero-title-block__metadata']")

    def get_movie_release_date(self):
        self.get_d1()
        d2 = self.d1.find_element(By.XPATH, "li[1]").text
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

    def get_movie_genre(self):
        print()

    def get_movie_rating(self):
        print()

    def get_all_movie_textdata(self):
        self.get_movie_links()
        for mt in self.links[:5]:
            self.driver.get(mt)
            self.get_movie_title()   
            self.get_movie_release_date()
            self.get_movie_age_rating()
            self.get_movie_runtime()
            self.get_movie_genre()
    
    def download_image(self):
        pass

    def download_image_from_tag(self, image_from_tag):
        pass

    def get_all_movie_imagedata(self):
        pass


if __name__ == "__main__":
    scraper = Scraper()

#%%
scraper.get_movie_title()
scraper.get_movie_release_date()
scraper.get_movie_age_rating()
scraper.get_movie_runtime()


#%%
scraper.get_all_movie_textdata()
#%%
scraper.driver.quit()
#%%
def accept_cookies():
    accept_button = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    accept_button.click()

