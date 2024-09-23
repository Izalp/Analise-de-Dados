import numpy as np


def missoes_sucesso(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str,
                      skiprows=1, encoding='utf-8')

    status_missao = data[:, -1]  # Última coluna

    # Contagem de quantas missões foram bem-sucedidas
    total_missoes = status_missao.shape[0]
    sucessos = np.sum(status_missao == 'Success')

    # Calculo da porcentagem de missões que deram certo
    porcentagem_sucessos = (sucessos / total_missoes) * 100
    return f"\nPorcentagem de missões que deram certo: {porcentagem_sucessos:.2f}%\n"


def gastos_missoes(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str,
                      skiprows=1, encoding='utf-8')

    custo = data[:, 6]  # 7º coluna

    # Filtrando as missões com custo maior que 0
    custos_disponiveis = custo[custo.astype(
        float) > 0].astype(float)

    # Cálculo da média dos custos
    if custos_disponiveis.size > 0:
        media_custos = np.mean(custos_disponiveis)
        return f"Média dos gastos das missões espaciais: ${media_custos:.2f}\n"
    else:
        return "Nenhum custo disponível para calcular a média.\n"


def missoes_eua(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str,
                      skiprows=1, encoding='utf-8')

    location = data[:, 2]  # 3º coluna

    # Filtrando as missões realizadas pelos EUA
    missoes_eua = np.sum(np.char.find(location, 'USA') != -1)
    return f"Total de missões realizadas pelos EUA: {missoes_eua}\n"


def missao_mais_cara(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str,
                      skiprows=1, encoding='utf-8')

    empresa = data[:, 1]  # 2º coluna

    # Filtrando as missões da SpaceX
    missoes_spacex = data[empresa == 'SpaceX']

    # Buscando a missão mais cara
    if missoes_spacex.size > 0:
        custos_spacex = missoes_spacex[:, 6].astype(float)
        index = np.argmax(custos_spacex)
        max_custo = missoes_spacex[index]

        missao_mais_cara = max_custo[4]
        custo_missao = custos_spacex[index]

        return f"A missão mais cara realizada pela SpaceX foi '{missao_mais_cara}' com um custo de ${custo_missao:.2f}\n"
    else:
        return "Nenhuma missão da SpaceX encontrada.\n"


def empresas_missoes(dataset):
    data = np.loadtxt(dataset, delimiter=';', dtype=str,
                      skiprows=1, encoding='utf-8')

    empresa = data[:, 1]  # 2º coluna

    # Buscando as empresas e suas quantidades de missões
    empresas, contagem_missoes = np.unique(empresa, return_counts=True)

    resultado = []
    for empresa, quantidade in zip(empresas, contagem_missoes):
        resultado.append(
            f"Empresa: {empresa} - Quantidade de Missões: {quantidade}")

    return '\n'.join(resultado)


# Carregar o dataset
dataset = 'data/space.csv'

# 1) Porcentagem de missões que deram certo
print(missoes_sucesso(dataset))

# 2) Média de gastos das missões
print(gastos_missoes(dataset))

# 3) Total de missões realizadas pelos EUA
print(missoes_eua(dataset))

# 4) Missão mais cara da SpaceX
print(missao_mais_cara(dataset))

# 5) Empresas e quantidades de missões
print(empresas_missoes(dataset))
