# Faça um programa que leia a largura e a altura de uma parede e calcule sua aréa e a quantidade de tinta necessaria para pinta-la (um litro de tinta pinta 2m²)
print('Descubra a area e a quantidade de tinta!')
l = float(input('Qual a largura da parede?: '))
alt = float(input('Qual a altura da parede?: '))
area = l * alt
lts = area / 2
print('A area da parede é de {}m² e a quantidade de tinta é de {} litros'.format (area, lts))