from abc import ABC, abstractmethod
import requests
from urllib.parse import urlencode, urlparse, parse_qs

class GeneralAPI(ABC):
    def __init__(self, core_url, items_per_page):
        self.core_url = core_url
        self.items_per_page = items_per_page
        self.url_dictionary = {}
        self.data = {}
        
    def add_url_to_dictionary(self, name, url):
        self.url_dictionary[name] = self.core_url + url

    @abstractmethod
    def compose_url(self, name, **kwargs):
        url = self.url_dictionary[name]
        if kwargs:
            url+= f'?{urlencode(kwargs)}'
        return url

    @abstractmethod
    def get(self, url):
        try:
            return requests.get(url)
        except Exception as e:
            print(e)
            return None
    
    