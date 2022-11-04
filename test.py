#%%
import requests # import the requests library
r = requests.get('http://pythonscraping.com/pages/page3.html') # make a HTTP GET request to this website
html_string = r.text # the text attribute of this response is the HTML as a string
print(r.text)
# %%
