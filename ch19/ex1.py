import requests
from bs4 import BeautifulSoup

#fetch page
url = 'https://www.wikipedia.org/'
response = requests.get(url)


#parse html
soup = BeautifulSoup(response.content, "html.parser")

#extract data
pgs = soup.find_all("p")
for pg in pgs:
    print(pg)


