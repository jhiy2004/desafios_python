times = ('Corinthians','Palmeiras','Santos','Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
        
print('-='*30)
print(f'Lista de times do Brasileirão: {times[0:]}')
print('-='*30)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f"O Chapecoense está na {times.index('Chapecoense')+1}° posição")