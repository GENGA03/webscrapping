import requests
from bs4 import BeautifulSoup
content_db = {}

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        if 'html' in response.headers.get('Content-Type'):
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text()
        elif 'json' in response.headers.get('Content-Type'):
            return response.json()
    return None


