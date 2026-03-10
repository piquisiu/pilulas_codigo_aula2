import math

#print = ("\n" + "-" * 50)
#assinantes = a
#mensalidade = m
#taxa = t
#meses = ms
#print = ("-" * 50)

#leituras
a = int(input('Digite a quantidades de assinantes: '))
m = float(input('Digite o valor da Mensalidade: '))
t = int(input('Digite a Taxa de Crescimento mensal %: ')) /100
ms = int(input('Digite a quantidade de meses da projeção: '))
#processamento
assinantes_finais = a * math.pow((1 + t), ms)
receita_final = assinantes_finais * m
#saida
print(f'Assinantes projetados: {assinantes_finais:.0f}')
print(f'Receita estimada: R$ {receita_final:.2f}')