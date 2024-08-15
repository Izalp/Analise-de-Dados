colocados = ['Argentina', 'França', 'Croácia', 'Marrocos', 'Inglaterra']

print('Os três primeiros colocados da Copa do Mundo FIFA de 2022:')
for i in range(3):
    print(f'{i+1}º - {colocados[i]}')

print('\nOs dois últimos colocados da Copa do Mundo FIFA de 2022:')
for i in range(-2, 0):
    print(f'{len(colocados) + i + 1}º - {colocados[i]}')

print(f'\nOs colocados em ordem alfabética: {sorted(colocados)}')

time_procurado = 'Barcelona'
if time_procurado in colocados:
    posicao = colocados.index(time_procurado) + 1
    print(f'\nO {time_procurado} está na posição {posicao}º.')
else:
    print(f'\nO {time_procurado} não está na colocação.')
