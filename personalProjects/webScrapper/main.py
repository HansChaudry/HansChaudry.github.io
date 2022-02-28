from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("img"):
    link_url = url + link["src"]
    print(link_url)