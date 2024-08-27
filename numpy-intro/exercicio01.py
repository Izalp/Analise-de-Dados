import numpy as np

print('QUESTÃO 01 - Criar um array de 21 valores igualmente espaçados entre 0 e 1\n')
array = np.linspace(0, 1, 21)
print(f'Array = {array}')

print('\nQUESTÃO 02 - Criar de dois arrays de números pares, concatenar e ordenar o array resultante\n')
array_pares1 = np.arange(0, 52, 2)
array_pares2 = np.arange(100, 51, -2)

res = np.concatenate((array_pares1, array_pares2))
res_ordenado = np.sort(res)
print(f'Array ordenado = {res_ordenado}')

print('\nQUESTÃO 03 - Ordenar o array resultante em ordem descrescente\n')
res_descrescente = np.sort(res)[::-1]
print(f'Array descrescente = {res_descrescente}')

print('\nQUESTÃO 04 - Criar uma matriz 3x4 e transformar a matriz em array de 1 dimensão\n')
matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
])

array_1d = matriz.flatten()
print(f'Array 1D = {array_1d}')

print('''\nQUESTÃO 05 - Mltiplicar o número de linhas pelo número de colunas de uma matriz e determinar 
      se o número total de elementos é par ou ímpar\n''')

matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
])

num_linhas, num_colunas = matriz.shape
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")

total_elementos = num_linhas * num_colunas
print(f"Total de elementos: {total_elementos}")

par_ou_impar = 'par' if total_elementos % 2 == 0 else 'ímpar'
print(f"O total de elementos é {par_ou_impar}\n")
