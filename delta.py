'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import math

a = float(input("Digte o primeiro valor:"))
if a == 0:
    print("Valor inválido")
else:
    b = float(input("Digite o segundo valor:"))
    c = float(input("Digite o terceiro valor:"))

delta = (b **2) - (4 *a *c)
print(delta)
if delta <0:
    print("A equação não possui números reais.")
elif delta == 0:
    print("A equaçao possui apenas uma raiz real.")
elif delta >0:
    print("A equação possui duas raízes.")