import datetime
data_compra = input('Data da compla (dd/mm/aaaa): ')
meses = int(input('Xem da galantia: '))
data_inicial = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days = meses * 30)
print(f'galantia valida até {data_final.strftime('%d/%m/%y')}')
print(f'dia da semana {data_final.strftime('%A')}')