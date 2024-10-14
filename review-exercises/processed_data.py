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


def cont_northern_america(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str, skiprows=1, encoding='utf-8')
    regions = data[:, 1] 
    regions = np.char.strip(regions) # removendo espaços extras 
    northern_america_count = np.sum(regions == 'NORTHERN AMERICA')

    print(f"\nNúmero de países na América do Norte (NORTHERN AMERICA): {northern_america_count}")


def max_gdp_latin_america(dataset):
    # Carregar os dados
    data = np.loadtxt(dataset, delimiter=';', dtype=str, skiprows=1, encoding='utf-8')
    
    data[:, 1] = np.char.strip(data[:, 1])  # removendo espaços extras da coluna de regiões
    
    latin_america_data = data[data[:, 1] == 'LATIN AMER. & CARIB']

    latin_america_data[:, 8] = np.char.strip(latin_america_data[:, 8]) # removendo espaços extras da coluna GDP 
    gdp_per_capita = latin_america_data[:, 8] 
    
    valid_gdp_mask = gdp_per_capita != '' # Filtra valores não vazios
    valid_gdp = gdp_per_capita[valid_gdp_mask]  
    
    print("\nPaíses encontrados na região LATIN AMER. & CARIB e seu respectivo GDP:")
    for i, country in enumerate(latin_america_data[valid_gdp_mask, 0]):
        print(f"{country}: {valid_gdp[i]}")

    valid_gdp = valid_gdp.astype(float)

    max_gdp_index = np.argmax(valid_gdp)
        
    # País correspondente ao maior GDP per capita
    max_gdp_country = latin_america_data[max_gdp_index, 0]
    print(f"\nPaís da América Latina e Caribe com maior renda per capita (GDP): {max_gdp_country}\n")


dataset = 'data/paises.csv'

# 1) Selecionando parte do dataset para mostrar "Country", "Region", "Population", "Area (sq. mi.)":
paises_output(dataset)

# 2) Contando as regiões no dataset:

cont_regioes(dataset)

# 3) Calculando a taxa média de alfabetização:
media_literacy(dataset)

# 4) Contando quantos países são da América do Norte (NORTHERN AMERICA):
cont_northern_america(dataset)

# 5) Encontrando o país com maior renda per capita na América Latina e Caribe:
max_gdp_latin_america(dataset)