from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import requests

r = requests.get('https://marshalledmakers.com/delete-later/')

