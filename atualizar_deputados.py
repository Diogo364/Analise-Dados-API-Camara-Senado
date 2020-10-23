from scripts.communication.camara import Camara


if __name__ == '__main__':
    
    camara = Camara()

    print('Buscando Todos os Deputados')
    deputados = camara.get_all('deputados')
    camara.generate_csv_for('deputados', './data')

