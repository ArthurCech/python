# escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salary = float(input('digite o salário do funcionário: R$ '))

if salary > 1250:
    final_salary = salary * 1.10
else:
    final_salary = salary * 1.15

# if reduzido
final_salary = salary * 1.10 if salary > 1250 else salary * 1.15

print('Salário reajustado: R$ {:.2f}'.format(final_salary))
