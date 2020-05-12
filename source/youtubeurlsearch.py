import urllib.request
from bs4 import BeautifulSoup

list_of_urls = []

textToSearch = 'corona information'

# urlify's the textToSearch
query = urllib.parse.quote(textToSearch)

# Constructs URL
url = "https://www.youtube.com/results?search_query=" + query

# Get's a response
response = urllib.request.urlopen(url)

# Saves response
html = response.read()

# Creates Soup Object
soup = BeautifulSoup(html, 'html.parser')

# Loops through
for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
    if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
        url = ('https://www.youtube.com' + vid['href'])
        list_of_urls.append(url)
