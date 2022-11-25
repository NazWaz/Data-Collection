# Data Collection

Data collection project.

## Milestone 1

Set up git repo and coding environment.

## Milestone 2

Chose a site to collect data from.

Holidays:
- Agoda
- Wego

Entertainment:
- Rotten Tomatoes
- IMDB
- SoundCloud
- Metacritic
- A-Z Animals

Ecommerce:
- Lego
- Square Enix
- Ikea
- Trustpilot
- Ocado
- Waterstones
- John Lewis

Health and Nutrition:
- MyProtein
- Lamberts
- Gorilla Mind

Finance:
- Coin Market


## Milestone 3

Created data scraper class and populated it with methods to extract links and scrape useful movie data.

![](../../../C:/AiCore/Data%20Collection%20Pipeline/Documentation/3/1.png)

- For this scraper code, the webdriver module from selenium and the By module needed to be imported.

![](../../../C:/AiCore/Data%20Collection%20Pipeline/Documentation/3/2.png)

- The class was set up and the driver was set as the Chrome webdriver. The url was the url for the IMDB top movies site. Using  `self.driver.get(url)`, I was able to load the url of the site I wanted to scrape data from. `time.sleep(2)` was used to add a delay when loading the site to actually load the page quicker - loading it too fast made the site think a bot is trying to access it.

![](../../../C:/AiCore/Data%20Collection%20Pipeline/Documentation/3/3.png)

- An empty list for the links was intialised using `self.links = []` and then a method was set up to scrape the site for all of the top movie links and placed them into a list. Using `movie_list = self.driver.find_element(By.XPATH, "//tbody[@class = 'lister-list']")`, an xpath for the block containing the list of movies was identified and set to the variable name movie_list. Then this was used to go further into the children of the xpath using `movies = movie_list.find_elements(By.XPATH, "tr/td/a")` where it searches for every xpath that has a `tr` then a `td` and then finally an `a` tag, which is where every link for each movie was located. Instead of find_element, find_elements was used as there were multiple xpaths to be found.

- In order to iterate through every xpath that has a link to a movie in the list, a for loop is used: `for movie in movies:`. Using `1 = movie.get_attribute("href")`, the link is assigned to the variable l in each iteration and an if loop `if 1 no in self.links:` checked to see if the link was already in the list. If it was not, it was added to the list using `self.links.append(l)` and this was neccessary to eliminate duplicate links.

- The final block, `if __name__ = "__main__":` was added to ensure the class could only be run directly when called and not just be imported. Then an instance of the class was set up using `scraper = Scraper()`.

![](../../../C:/AiCore/Data%20Collection%20Pipeline/Documentation/3/4.png)

- The get_movie_links() method was called using `scraper.get_movie_links()` and a list of the links was printed to check the output using `print(scraper.links)`.


## Milestone 4



## Milestone 5



## Milestone 6



# Milestone 7