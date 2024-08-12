import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    else:
        raise Exception(f"Failed to retrieve content. Status code: {response.status_code}")