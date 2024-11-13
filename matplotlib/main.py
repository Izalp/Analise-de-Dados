import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def grafico_empresas(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    empresas_eua = data[data['Location'].str.contains('USA')]['Company Name'].unique()
    empresas_china = data[data['Location'].str.contains('China')]['Company Name'].unique()

    plt.figure(figsize=(8, 6))
    plt.bar(['USA', 'China'], [len(empresas_eua), len(empresas_china)], color=['blue', 'red'], width=0.5)
    plt.xlabel('País')
    plt.ylabel('Número de Empresas')
    plt.title('Quantidade de Empresas Espaciais - USA vs China')
    plt.show()


def graficos_taxas(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    america_norte = data[data['Region'].str.contains('NORTHERN AMERICA')]
    birthrate = america_norte['Birthrate']
    deathrate = america_norte['Deathrate']

    plt.figure(figsize=(10, 6))
    plt.plot(birthrate, label='Taxa de Natalidade (Birthrate)', color='blue', marker='o')
    plt.plot(deathrate, label='Taxa de Mortalidade (Deathrate)', color='red', marker='o')
    plt.xlabel('Países da América do Norte')
    plt.ylabel('Taxa')
    plt.title('Taxa de Natalidade e Mortalidade - América do Norte')
    plt.legend()
    plt.show()


space = "./data/space.csv"
paises = "./data/paises.csv"

# Questão 1) Gráfico em barras - quantidade de empresas dos EUA e CHINA:
grafico_empresas(space)

# Questão 2) Gráficos de linhas - taxas Birthrate e Deathrate da America do Norte:
graficos_taxas(paises)