magazineLuiza = {'Samsung Galaxy S23 Ultra', 'Apple iPhone 14 Pro',
                 'Xiaomi Redmi Note 12 Pro', 'Motorola Moto G62', 'Samsung Galaxy A54'}
fastShop = {'Samsung Galaxy Z Fold 4', 'Apple iPhone 13',
            'Samsung Galaxy A54', 'Motorola Edge 30 Pro', 'Xiaomi Redmi Note 12 Pro'}

todos_modelos = magazineLuiza.union(fastShop)
modelos_em_ambas = magazineLuiza.intersection(fastShop)

print('\nTodos os modelos disponíveis se visitar ambas as lojas:')
for modelo in todos_modelos:
    print(f'- {modelo}')

print('\nModelos disponíveis em ambas as lojas:')
for modelo in modelos_em_ambas:
    print(f'- {modelo}')
