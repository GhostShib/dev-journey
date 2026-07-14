# Faça um algoritimo que leia o valor de um produto e mostre seu novo preço com 5% de desconto
print('Calcule o desconto de 5%!')
preco = float(input('Qual o Valor do produto '))
dez = preco / 10
desconto = dez / 2
preco_final = preco - desconto
print('O preço com desconto é de {} Reais!'.format (preco_final))