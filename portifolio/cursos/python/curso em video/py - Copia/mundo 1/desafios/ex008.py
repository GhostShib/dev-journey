# crie um programa que leia um valor em metros e converta em centimetros e milimetros
# até a aula 7
print('converta metros para cm e mm!')
m = float(input('Quantidade de metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('Em {} metros cabe\n{} km\n{} hm\n{} Dam\n{} dm\n{} cm\n{} mm'.format(m, km, hm, dam, dm, cm, mm))




