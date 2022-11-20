
import requests
from bs4 import BeautifulSoup
from uuid import uuid4
import pandas as pd

class ProductScraper():
    '''
    Scrapers webpage for data.

    Attributes:
    ----------
    page_url: str
        URL for the website being scraped
    '''
    def __init__(self):
        self.df = pd.DataFrame(columns=["id", "name", "description", "price"])

    def get_homepage(self):
        '''
        Gets html data from site.
        '''
        self.page_url = 'http://pythonscraping.com/pages/page3.html'
        response = requests.get(self.page_url) # makes a HTTP get request to the website
        html = response.content # content attribute of the response is HTML as a string
        html = BeautifulSoup(html, 'html.parser') # Convert that into a BeautifulSoup object that contains methods to make the tag search easier
        print(html.prettify())
        return html

    def get_products(self, html):
        '''
        Gets rows of products from html.
        '''
        return html.find_all("tr")[1:] # finds all rows in table

    def download_img(self, img_url, fp):
        '''
        Downloads images from url
        '''
        img_data = requests.get(img_url).content
        with open(fp, 'wb') as handler:
            handler.write(img_data)

    def get_all_product_data(self):
        '''
        Gets all product data. 
        '''
        html = self.get_homepage()
        products = self.get_products(html)
        for product in products:
            self.get_product_data(product)

        print(self.df)
        self.df.to_csv("Demos/tabular_data.csv") # outputs table into csv file
        
    def get_product_data(self, product):
        '''
        Gets individual product data in the form of id, name, desc, price, img.
        '''
        id = product.attrs["id"]

        data = product.find_all("td") # finds all td data types
        img = data.pop() # removes image link
        img_src = img.img.attrs["src"] # gets relative path for image

        img_src = self.page_url[:-16] + img_src[3:]
        print(img_src)
        self.download_img(img_src, f"Demos/Images_1/{id}.jpg")
                
        data = [feature.text for feature in data]
        title, description, price = data

        product_data = pd.DataFrame({ 
            "id": [id],
            "name": [title], 
            "description": [description], 
            "price": [price], 
            #"img": Demos/Images_1 
        })
        self.df = pd.concat([self.df, product_data]) # combines headers and table

if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.get_all_product_data()
