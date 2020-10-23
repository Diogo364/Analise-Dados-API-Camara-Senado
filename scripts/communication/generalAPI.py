from abc import ABC, abstractmethod
from scripts.messages.feedback import Feedback
import requests
import pandas as pd
from urllib.parse import urlencode, urlparse, parse_qs, quote

class GeneralAPI(ABC, Feedback):
    def __init__(self, core_url, items_per_page):
        self.core_url = core_url
        self.items_per_page = items_per_page
        self.url_dictionary = {}
        self.data = {}
        
    def _add_url_to_dictionary(self, name, url):
        self.url_dictionary[name] = self.core_url + url

    @abstractmethod
    def _compose_url(self, name, mandatory_params=None, get_parameters=None):
        url = self.url_dictionary[name]
        print(url)
        if mandatory_params:
            url = url.format(*mandatory_params)
        if get_parameters:
            url+= f'?{urlencode(get_parameters)}'
        print(url)
        return quote(url, safe='/:&=?')

    @abstractmethod
    def get(self, url):
        try:
            return requests.get(url)
        except Exception as e:
            print(e)
            return None
    
    @abstractmethod
    def get_data(self, name):
        try:
            print(self.data[name])
        except KeyError:
            self._print_no_data_message(name)

    @abstractmethod
    def generate_csv_for(self, name, PATH):
        try:
            self.data[name].to_csv(f'{PATH}/{name}.csv', index=False)
        except KeyError:
            self._print_no_data_message(name)


    def create_dataframe_from_response(self, list_of_dicts):
        return pd.DataFrame(list_of_dicts)