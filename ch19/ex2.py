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

# find_all() method
# Find all occurrences of a h2
soup.find_all("h2")  
# Find all h3 tags with id of main
soup.find_all("h3", id="main")
# Find all occurrences of a specific text  
soup.find_all(text="text to find")  

# select() method
# Select all elements with class "colour"
elements = soup.select(".colour")
# Select the element with ID "main"
element = soup.select("#main")
# Select all <a> tags within a <div> element with class "container"
links = soup.select("div.container a")

# get() method
# get the value of the 'href' attribute
link = soup.find('a')
href_text = link.get('href')
print("URL:", href_text)

# get the 'class' attribute of an element
element = soup.find('div')
class_value = element.get('class')
print(class_value)

# text attribute
tags = soup.find_all("a")
for tag in tags:
    tag_text = tag.text
    print(tag_text)
