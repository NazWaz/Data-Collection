#%%
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os

#%%
class LyricScraper():
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://genius.com/#top-songs")
        self._accept_cookies()

    def _accept_cookies(self):
        accept_button = self.driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        accept_button.click()

    def get_song_links(self):
        charts = self.driver.find_element(By.XPATH, "//div[@id='top-songs']")
        songs = charts.find_elements(By.XPATH, "div/div/a") 
        return [song.get_attribute("href") for song in songs]

    def get_lyrics(self):
        lyrics = self.driver.find_element(By.XPATH, "//div[@data-lyrics-container='true']").text
        song_name = self.driver.current_url.split("/")[-1]
        filename = os.path.join("Lyricsdata", f"{song_name}.txt")
        with open(filename, "w") as f:
            f.write(lyrics)

    def get_all_song_lyrics(self):

        song_links = self.get_song_links()

        for song_link in song_links:
            self.driver.get(song_link)
            self.get_lyrics()

scraper = LyricScraper()
#%%

scraper.get_all_song_lyrics()
scraper.driver.quit()

# %%
