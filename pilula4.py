import statistics as s
lote1 = float(input('Produção lote 1: '))
lote2 = float(input('Produção lote 2: '))
lote3 = float(input('Produção lote 3: '))
media = s.mean( (lote1, lote2, lote3) )
desvio = s.stdev( (lote1, lote2, lote3) )
print(f'Media: {media:.2f}')
print(f'Desvio padrão: {desvio:.2f}')