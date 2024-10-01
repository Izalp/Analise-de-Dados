import numpy as np


def paises_output(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str, skiprows=1, encoding='utf-8')
    output = data[:, [0, 1, 2, 3]]  
   
    print("\nPaís, Região, População, Área (milhas quadradas):")
    for row in output:
        print(f"País: {row[0]}, Região: {row[1]}, População: {row[2]}, Área: {row[3]} sq. mi.")


def cont_regioes(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str, skiprows=1, encoding='utf-8')
    regions = data[:, 1]  # 
    unique_regions, counts = np.unique(regions, return_counts=True)

    print("\nContagem por Região:")
    for region, count in zip(unique_regions, counts):
        print(f"Região: {region}, Contagem: {count}")


def media_literacy(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str, skiprows=1, encoding='utf-8')
    literacy_rates = data[:, 9]  
    
    literacy_rates = literacy_rates[literacy_rates != '']
    literacy_rates = literacy_rates.astype(float)
    avg_literacy = np.mean(literacy_rates)

    print(f"\nTaxa média de alfabetização: {avg_literacy:.2f}%")
    return avg_literacy


dataset = 'data/paises.csv'

# 1) Selecionando parte do dataset para mostrar "Country", "Region", "Population", "Area (sq. mi.)":
paises_output(dataset)

# 2) Contando as regiões no dataset:
cont_regioes(dataset)

# 3) Calculando a taxa média de alfabetização:
media_literacy(dataset)
