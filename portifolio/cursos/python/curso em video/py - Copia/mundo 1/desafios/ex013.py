# crie um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
print('Veja seu salario após o aumento!')
salario = float(input('Digite seu salario atual: '))
aumento = salario * 0.15
final = aumento + salario
print('Seu novo salario é de {} Reais!'.format (final))