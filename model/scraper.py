import requests
from bs4 import BeautifulSoup


def scrape_filename(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
    # filenames = [item.text for item in soup.find_all("a", class_="filenames")]
    # return filenames


url = "https://www.1377x.to/series/allegiance/1/13/"
filenames = scrape_filename(url)
print(filenames)
