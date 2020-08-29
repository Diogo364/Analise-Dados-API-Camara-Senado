import pprint
import json
import pandas as pd
from scripts.communication.generalAPI import GeneralAPI
from urllib.parse import urlencode, urlparse, parse_qs

class Camara(GeneralAPI):
  def __init__(self):
    super().__init__(
      core_url='https://dadosabertos.camara.leg.br/api/v2', 
      items_per_page=100
    )
    self.add_url_to_dictionary('deputados', '/deputados')
    
  
  def compose_url(self, name, **kwargs):
    return super().compose_url(name, **kwargs)

  def success_message_for(self, message):
    return (f'Successfuly get {message}')

  def get(self, name, items_per_page=None, verbose=1, **kwargs):
    if not items_per_page:
      items_per_page = self.items_per_page
    url = self.compose_url(name, itens=items_per_page, **kwargs)
    response = super().get(url)
    if response:
      if verbose:
        print(self.success_message_for(name))
      dict_response = json.loads(response.text)
      self.data[name] = self.create_dataframe_from_response(dict_response['dados'])
      return dict_response
      
  
  def create_dataframe_from_response(self, list_of_dicts):
    return pd.DataFrame(list_of_dicts)
  
  def get_page_from_url(self, url):
        parsed = urlparse(url)
        return parse_qs(parsed.query)['pagina']

  def get_ref_links(self, links_list_json):
    ref_links = {}
    for link in links_list_json:
      ref_links[link['rel']] = link['href']
    return ref_links

  def get_all(self, name,verbose=1, items_per_page=None):
    response_data = []
    page = 1
    while True:
      response = self.get(name, items_per_page, verbose=0, pagina=page)
      response_data.extend(response['dados'])
      ref_links = self.get_ref_links(response['links'])
      if 'last' not in ref_links.keys():
        break
      page+=1
    if verbose:
      print(self.success_message_for(name))
    self.data[name] = self.create_dataframe_from_response(response_data)
    return response_data

  def no_data_message(self, name):
    return (f'No data on {name}')

  def get_data(self, name):
    try:
      print(self.data[name])
    except:
      print(self.no_data_message(name))

  def generate_csv_for(self, name, PATH):
    try:
      self.data[name].to_csv(f'{PATH}/{name}.csv', index=False)
    except:
      print(self.no_data_message(name))
