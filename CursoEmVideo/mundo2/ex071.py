# crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

qtd50 = qtd20 = qtd10 = qtd1 = 0

money = int(input('digite o valor que deseja sacar: '))

qtd50 = money // 50 % 50
rest = money % 50
qtd20 = rest // 20 % 20
rest = rest % 20
qtd10 = rest // 10 % 10
qtd1 = rest % 10

print(f'Qtd. de notas de R$ 50: {qtd50}')
print(f'Qtd. de notas de R$ 20: {qtd20}')
print(f'Qtd. de notas de R$ 10: {qtd10}')
print(f'Qtd. de notas de R$ 1: {qtd1}')




# método guanabara
money = int(input('digite o valor que deseja sacar: R$ '))
total = money
banknotes = 50
totbanknotes = 0
while True:
    if total >= banknotes:
        total -= banknotes
        totbanknotes += 1
    else:
        if totbanknotes > 0:
            print(f'Total de {totbanknotes} cédulas de R$ {banknotes}')
        if banknotes == 50:
            banknotes = 20
        elif banknotes == 20:
            banknotes = 10
        elif banknotes == 10:
            banknotes = 1

        totbanknotes = 0

        if total == 0:
            break