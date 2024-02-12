# BeautifulSoup Methods and attributes

import requests
from bs4 import BeautifulSoup

url = 'https://www.wikipedia.org/'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# find() method

# Find the first occurrence of a h1 tag
soup.find("h1")

# Find a h2 tag with an id="main"
soup.find("h2", id="main")

# Find a specific text within the document
soup.find(text="text to find")
