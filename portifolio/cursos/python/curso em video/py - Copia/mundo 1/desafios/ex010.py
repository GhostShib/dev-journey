# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar (US$ = 3,27)
print('Venha converter!')
d = float(input('Quanto dinheiro você tem?: '))
us = d / 3.27
print('Com {} Reais você pode comprar {} Doláres!'.format (d, us) )