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

    def get_movie_links(self):
        movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")
        movies = movie_list.find_elements(By.XPATH, "tr/td/a")
        for movie in movies:
            l = movie.get_attribute("href")
            if l not in self.links:
                self.links.append(l)

if __name__ == "__main__":
    scraper = Scraper()

#%%
scraper.get_movie_links()
print(scraper.links)
# %%
