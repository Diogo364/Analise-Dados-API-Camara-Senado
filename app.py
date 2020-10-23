import streamlit as st
import os
import numpy as np
import pandas as pd
from termcolor import colored
from matplotlib import pyplot as plt
import seaborn as sns





print(colored('\n\n\tAccess through: localhost:8501', 'blue'))


deputados = None

'''
# Análise dados Parlamentares

O objetivo desse projeto é trazer informações e insights a respeito da atuação e composição dos parlamentares.
'''

# if st.button('Atualize os dados de deputados'):
#     st.text('Atualizando dados...')
#     os.system('python atualizar_deputados.py')
#     try:
#         deputados = pd.read_csv('data/deputados.csv')
#         st.dataframe(deputados.head())
#     except (FileNotFoundError, FileExistsError):
#         st.text('Arquivo não encontrado, tente novamente!')

deputados = pd.read_csv('data/deputados.csv')


st.dataframe(deputados.head())

if deputados is not None:
    fig, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].set_title('Partido')
    sns.countplot(y=deputados.siglaPartido, order=deputados.siglaPartido.value_counts().index, ax=ax[0], color='orange')
    ax[1].set_title('UF')
    sns.countplot(y=deputados.siglaUf, order=deputados.siglaUf.value_counts().index, ax=ax[1], color='lightgreen')
    fig.suptitle('Distribuições')
    st.pyplot(fig)