import pprint
import json
import pandas as pd
from urllib.parse import urlencode, urlparse, parse_qs
from scripts.communication.generalAPI import GeneralAPI

class Camara(GeneralAPI):
  def __init__(self):
    super().__init__(
      core_url=r'https://dadosabertos.camara.leg.br/api/v2', 
      items_per_page=100
    )
    self._add_url_to_dictionary('deputados', '/deputados')
    self._add_url_to_dictionary('despesas', '/deputados/{}/despesas')
  
  def _compose_url(self, name, mandatory_params, get_parameters):
    return super()._compose_url(name, mandatory_params, get_parameters)

  def get(self, name, mandatory_params=None, get_parameters={}, verbose=1):
    if 'itens' not in get_parameters.keys():
      get_parameters['itens'] = self.items_per_page
    url = self._compose_url(name, mandatory_params, get_parameters)
    print(url)
    response = super().get(url)
    if response:
      if verbose:
        self._print_success_message_for_get(name)
      dict_response = json.loads(response.text)
      self.data[name] = self.create_dataframe_from_response(dict_response['dados'])
      return dict_response
      
  def __get_page_from_url(self, url):
        parsed = urlparse(url)
        return parse_qs(parsed.query)['pagina']

  def __get_ref_links(self, links_list_json):
    ref_links = {}
    for link in links_list_json:
      ref_links[link['rel']] = link['href']
    return ref_links

  def get_all(self, name, mandatory_params=None, get_parameters={}, verbose=1):
    response_data = []
    page = 1
    while True:
      response = self.get(name, mandatory_params, get_parameters={**get_parameters, 'pagina': page}, verbose=0)
      response_data.extend(response['dados'])
      ref_links = self.__get_ref_links(response['links'])
      if 'last' not in ref_links.keys():
        break
      page+=1
    if verbose:
      self._print_success_message_for_get(name)
    self.data[name] = self.create_dataframe_from_response(response_data)
    return response_data

  def get_data(self, name):
    super().get_data(name)

  def generate_csv_for(self, name, PATH):
    super().generate_csv_for(name, PATH)
