import numpy as np

print('QUESTÃO 01)\n')
np.random.seed(5)

array_floats = np.random.uniform(-1, 1, 10)

array_multiplicado = array_floats * 100
array_inteiro = np.floor(array_multiplicado).astype(int)

print(f'Array de floats: {array_floats}\n')
print(f'Array multiplicado por 100: {array_multiplicado}\n')
print(f'Array com a parte inteira: {array_inteiro}\n')

print('QUESTÃO 02)\n')
np.random.seed(10)

matriz = np.random.randint(1, 51, size=(4, 4))
print('Matriz 4x4:')
print(matriz)

print('\nQUESTÃO 03)\n')
np.random.seed(10)

matriz = np.random.randint(1, 51, size=(4, 4))

media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

maior_linhas = np.max(media_linhas)
maior_colunas = np.max(media_colunas)

print(f'Média de cada linha: {media_linhas}\n')
print(f'Média de cada coluna: {media_colunas}\n')
print(f'Maior valor das médias das linhas: {maior_linhas}\n')
print(f'Maior valor das médias das colunas: {maior_colunas}\n')

print('QUESTÃO 04)\n')
np.random.seed(10)

matriz = np.random.randint(1, 51, size=(4, 4))
valores, contagens = np.unique(matriz, return_counts=True)
numeros_2_vezes = valores[contagens == 2]

print("Matriz 4x4:")
print(matriz)

print('\nNúmero de aparições de cada número:\n')
aparicoes = dict(zip(valores, contagens))

for numero, contagem in aparicoes.items():
    print(f'Número {numero}: {contagem} vez(es)')

print(f'\nNúmeros que aparecem exatamente 2 vezes: {numeros_2_vezes}\n')
