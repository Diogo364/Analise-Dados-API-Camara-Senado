from scripts.communication.camara import Camara
import pandas as pd
import pprint

camara = Camara()
camara.get_data('deputados')
deputados = camara.get_all('deputados')
camara.generate_csv_for('deputados', './data')

