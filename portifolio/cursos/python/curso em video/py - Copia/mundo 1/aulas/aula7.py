# operadores aritméticos
''' Operadores:
+ == Adição
- == Subtração
* == Multiplicação
/ == Divisão
** == Potencia
// == Divisão Inteira
% == Resto da Divisão
X**(1,2) == Raiz Quadrada

'''
''' Ordem De Precedencia:
1) ()
2) **
3) *, /, //, % (Oque aparecer primeiro)
4) +, -
'''
'''
nome = input('Qual o seu nome? ')
print('Prazer em conhecer {:=^20}'.format(nome))
'''
n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma de {} e {} é igual a {}\nO produto é {} \nA divisão é {}'.format (n1, n2, s, m, d), end=' ' )
print('\nA divisão inteira é {}\nE a potencia é {}'.format (di, e))