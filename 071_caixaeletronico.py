# Calcula a quantidade de notas de cada valor a serem sacadas em uma caixa eletrônico
print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)
valor = int(input('Valor a ser sacado: R$ '))
# notas de real (R$) existentes
tot200 = valor // 200
tot100 = (valor % 200) // 100
tot50 = ((valor % 200) % 100) // 50
tot20 = (((valor % 200) % 100) % 50) // 20
tot10 = ((((valor % 200) % 100) % 50) % 20) //10
tot5 = (((((valor % 200) % 100) % 50) % 20) % 10) // 5
tot2 = ((((((valor % 200) % 100) % 50) % 20) % 10) % 5) // 2
while True:
    if tot200 > 0:
        print(f'Total de {tot200} cédula(s) de R$ 200,00.')
    if tot100 > 0:
        print(f'Total de {tot100} cédula(s) de R$ 100,00.')
    if tot50 > 0:
        print(f'Total de {tot50} cédula(s) de R$ 50,00.')
    if tot20 > 0:
        print(f'Total de {tot20} cédula(s) de R$ 20,00.')
    if tot10 > 0:
        print(f'Total de {tot10} cédula(s) de R$ 10,00.')
    if tot5 > 0:
        print(f'Total de {tot5} cédula(s) de R$ 5,00.')
    if tot2 > 0:
        print(f'Total de {tot2} cédula(s) de R$ 2,00.')
    break
