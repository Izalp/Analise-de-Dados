import pandas as pd


def paises_oceania(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    paises = data[data['Region'].str.contains('OCEANIA')]
    quant_paises = paises.shape[0]

    print('Países da Oceania:')
    print(paises[['Country']].to_string(index=False))
    print(f"\nNúmero de países na Oceania: {quant_paises}")


def media_literacy(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    media_taxa = pd.to_numeric(data['Literacy (%)']).mean()

    print(f'\nMédia da taxa de alfabetização: {media_taxa:.2f}%')
    

def maior_populacao(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    populacao_max = data['Population'].max()
    pais_maior_populacao = data[data['Population']==populacao_max]
    pais_e_regiao = pais_maior_populacao[['Country', 'Region']]

    print("\nPaís com a maior população e sua região:")
    print(pais_e_regiao.to_string(index=False))


def paises_sem_costa(dataset):
    data = pd.read_csv(dataset, delimiter=';')
    paises = data[data['Coastline (coast/area ratio)'] == 0]
    paises[['Country']].to_csv('noCoast.csv', index=False)
    
    print('\nPaíses sem Costa Marítima:')
    print(paises[['Country']].to_string(index=False))
    print("\nArquivo salvo com sucesso!")


dataset = 'paises.csv'

# 1) Mostrar os países da Oceania e a quantidade de países da Oceania:
paises_oceania(dataset)

# 2) Mostrar a média da taxa de alfabetização:
media_literacy(dataset)

# 3) País que possui maior população e sua região:
maior_populacao(dataset)

# 4) Paises que não possuem costa maritima:
paises_sem_costa(dataset)