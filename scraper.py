#%%
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from unidecode import unidecode

import time
import os
import requests
import json

class Scraper():
    '''
    A top movie list data scraper that scrapes all the useful data for the top 250 movies from the IMDB website.

    Attributes
    ----------
    driver: str
        Loads the Chrome webdriver to be used with the Selenium commands.
    links: list
        A list of url links for each movie.
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
    images: list
        A list of images for each movie.

    Methods
    -------
    get_movie_links
        Scrapes website for all top movie url links.
    get_id
        Uses top movie url link to generate unique ids for each data entry.
    get_timestamp
        Generates timestamp for when the data for each movie is scraped in the form of d-m-Y_H:M:S.
    get_movie_title
        Scrapes movie title.
    get_release_age_runtime_xpath
        Scrapes for xpath of the block containing movie release date, rating and runtime.
    get_movie_release_date
        Scrapes movie release date.
    get_movie_age_rating
        Scrapes movie age rating.
    get_movie_runtime
        Scrapes movie runtime.
    get_movie_genre
        Scrapes movie genre.
    get_movie_rating 
        Scrapes movie rating.
    get_movie_image
        Scrapes movie image source link.
    get_image_tag
        Gets image content and generates image tag.
    download_image_data
        Downloads image locally to an images folder as a jpg file.
    download_text_data
        Downloads data dictionaries locally to a raw_data folder as a json file.
    get_all_movie_data
        Scrapes every top movie site for data and stores it locally.
    '''
    def __init__(self):
        '''
        Constructs all the neccessary attributes for the scraper object. 
        Loads the IMDB top 250 movie site using Selenium.
        '''

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options = self.__create_options())
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
        self.images = []   

    def __create_options(self):
        
        chrome_options = webdriver.ChromeOptions()
    
        chrome_options.add_argument("--headless");
        chrome_options.add_argument("--test-type");
        chrome_options.add_argument("--disable-gpu");
        chrome_options.add_argument("--no-first-run");
        chrome_options.add_argument("--no-default-browser-check");
        chrome_options.add_argument("--ignore-certificate-errors");
        chrome_options.add_argument("--start-maximized");
        
        
        return chrome_options


    def get_movie_links(self) -> None:
        '''
        Scrapes the top IMDB movies site for every top movie url link by first finding the XPATH 
        containing the list of top movies and then finding a list of XPATHs containing the individual url links.
        A for loop is used to iterate through each XPATH with the url links to take each one and append it to a list
        if it is not already present (to avoid duplicates).
        '''

        movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")
        movies = movie_list.find_elements(By.XPATH, "tr/td/a")
        for movie in movies:
            movie_url = movie.get_attribute("href")
            if movie_url not in self.links:
                self.links.append(movie_url)
    
    def get_id(self, movie_link:str) -> None:
        '''
        Uses the url link for each movie and takes the last element as an integer to generate a unique id for each movie.
        This id is the same as the ranking for each movie in the list of top movie.
        The get_timestamp method is also called to get a timestamp for when the data scraping on a movie page begins.
        Finally, each id is added to a list of ids.

        Parameters
        ----------
        movie_link: str
            The url link for each movie.
        '''

        self.id = int(movie_link.rsplit("_", 1)[-1])
        self.get_timestamp()
        self.ids.append(self.id)

    def get_timestamp(self) -> None:
        '''
        Takes the timestamp and converts it into a date time format in the form d-m-Y_H:M:S.
        Each timestamp is added to a list of timestamps.
        '''

        timestamp = time.time()
        datetimestamp = datetime.fromtimestamp(timestamp)
        self.datetime = datetimestamp.strftime("%d-%m-%Y_%H:%M:%S")
        self.timestamps.append(self.datetime)
        
    def get_movie_title(self) -> None:
        '''
        Scrapes the movie site for the movie title, taking the text element of the title heading XPATH.
        Each title is added to a list of titles.
        '''
        title = WebDriverWait(self.driver,0).until(EC.presence_of_element_located((By.XPATH, "//h1[@data-testid = 'hero-title-block__title']"))).text
        title = unidecode(title)
        self.titles.append(title)

    def get_release_age_runtime_xpath(self) -> None:
        '''
        Scrapes the movie site for the unordered list XPATH containing all the release date, age rating and runtime.
        Used to access this list's XPATH easily later.
        '''

        self.release_age_runtime_xpath = self.driver.find_element(By.XPATH, "//ul[@data-testid = 'hero-title-block__metadata']")

    def get_movie_release_date(self) -> None:
        '''
        Scrapes the movie site for the movie release date, taking the text element of the first list item in the XPATH.
        The release date is set to an integer value also.
        Each release date is added to a list of release dates.
        '''

        release_date = int(self.release_age_runtime_xpath.find_element(By.XPATH, "li[1]").text)
        self.release_dates.append(release_date)

    def get_movie_age_rating(self) -> None:
        '''
        Scrapes the movie site for the movie age rating, taking the text element of the second list item in the XPATH.
        Each age rating is added to a list of age ratings.
        '''

        age_rating = self.release_age_runtime_xpath.find_element(By.XPATH, "li[2]").text
        self.age_ratings.append(age_rating)

    def get_movie_runtime(self) -> None:
        '''
        Scrapes the movie site for the movie runtime, taking the text element of the third list item in the XPATH.
        Each runtime is added to a list of runtimes.
        '''

        runtime = self.release_age_runtime_xpath.find_element(By.XPATH, "li[3]").text
        self.runtimes.append(runtime)

    def get_movie_genre(self) -> None:
        '''
        Scrapes the movie site for the movie genre/s by first finding the container XPATH for all genres.
        Using try and except blocks, the text elements of all 3 HTML XPATHS is set to 3 genres then combined 
        into a list of genres and then joined together into a string with a "/" seperator.
        If there are only 2 genres, the text elements of the first 2 HTML XPATHS is set to 2 genres then
        combined into a list of genres and then joined together into a string with a "/" seperator.
        If there is only 1 genre, the text element of the first HTML XPATH is set to the genre.
        Each genre is added to a list of genres.
        '''

        genre_xpath = self.driver.find_element(By.XPATH, "//div[@class = 'ipc-chip-list__scroller']")
        try:
            genre_1 = genre_xpath.find_element(By.XPATH, "a[1]").text
            genre_2 = genre_xpath.find_element(By.XPATH, "a[2]").text
            genre_3 = genre_xpath.find_element(By.XPATH, "a[3]").text
            genre_all = [genre_1, genre_2, genre_3]
            genre = "/".join(genre_all)
        except:
        
            try:
                genre_1 = genre_xpath.find_element(By.XPATH, "a[1]").text
                genre_2 = genre_xpath.find_element(By.XPATH, "a[2]").text
                genre_all = [genre_1, genre_2]
                genre = "/".join(genre_all)
        
            except:
                genre = genre_xpath.find_element(By.XPATH, "a[1]").text
        self.genres.append(genre)
        
    def get_movie_rating(self) -> None:
        '''
        Scrapes the movie site for the movie rating by first finding the text element of the container XPATH for the rating.
        The rating is the first element of the XPATH text before the "/" and set as a float value.
        Each rating is added to a list of ratings.  
        '''

        rating_xpath = self.driver.find_element(By.XPATH, "//div[@data-testid = 'hero-rating-bar__aggregate-rating__score']").text
        rating = float(rating_xpath.rsplit("/", 1)[0])
        self.ratings.append(rating)

    def get_movie_image(self) -> None:
        '''
        Scrapes the movie site for the image poster of the movie by finding the image XPATH and taking the image source link.
        Each image link is added to a list of images.
        The image link is also returned when calling this function.
        '''

        image_xpath = self.driver.find_element(By.XPATH, "//img")
        image = image_xpath.get_attribute("src")
        self.images.append(image)
        return image
        
    def get_image_tag(self) -> None:
        '''
        The image data is taken from the image source link.
        A tag is generated for each image in the format date_time_id.jpg.
        '''

        os.makedirs("raw_data/images", exist_ok = True)
        image_url = self.get_movie_image()
        self.image_data = requests.get(image_url).content
        image_datetime = self.datetime.replace("-", "").replace(":", "")
        image_id = str(self.id)
        self.image_tag = image_datetime + "_" + image_id

    def download_image_data(self) -> None:
        '''
        Downloads the image locally to an images folder in a root folder "raw_data" using the image source link.
        '''
        
        with open(f"raw_data/images/{self.image_tag}.jpg", 'wb') as handler:
            handler.write(self.image_data)

    def download_text_data(self) -> None:
        '''
        Downloads the dictionary containing all the movie data locally as a json file in a root folder "raw_data".
        '''

        os.makedirs("raw_data", exist_ok = True)
        with open("raw_data/data.json", "w") as fp:
            json.dump(self.data, fp, indent = 4)

    def get_all_movie_data(self, no_of_movies) -> None:
        '''
        Calls all the data scraping methods in one method to collect data from every top movie site.
        Gets a list of each movie link and iterates through every scraping method using a for loop, loading each movie page.
        Scrapes all text and image data, stores them in a dictionary and saves the images and dictionary locally.
        The dictionary of data contains the id, timestamp, title, release date, age rating, runtime, genre, rating and image. 
        '''

        self.get_movie_links()
        for movie_link in self.links[:no_of_movies]:
            self.driver.get(movie_link)
            self.get_id(movie_link)
            self.get_movie_title()   
            self.get_release_age_runtime_xpath()
            self.get_movie_release_date()
            self.get_movie_age_rating()
            self.get_movie_runtime()
            self.get_movie_genre()
            self.get_movie_rating()
            self.get_image_tag()
            self.download_image_data()
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
        
    def exit(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    scraper = Scraper()
    scraper.get_movie_links()
    scraper.driver.get(scraper.links[0])
    scraper.get_movie_title()
    print(scraper.titles)
    scraper.exit()
# %%
