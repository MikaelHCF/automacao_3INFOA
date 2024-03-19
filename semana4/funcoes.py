'''
As funções permite modularizar o código, dividir ele em partes menore que podem ser reaproveitada. Isso simplifica a codificação.

Estrutura função em python

def nome_função(param1, paam2, paramN)
    //algum código que a função faz return
    return valor_retornado

'''

#cria uma função que calcula a área do triângulo

def calculateTriangreArea(base, altura):
    area = (base * altura) / 2
    return area

#cria uma função que calcula a área do quadrado

def calculateSquareArea(lado):
    area = lado * lado
    return area

'''
#Exemplo 1 : chamar a função

area1 = calculateTriangreArea(100, 10)
print("A área do triangulo 1 é ", area1)

#Exemplo 2 : chamar a função novamente

base = float(input('Digite a base : '))
altura = float(input('Digita a altura : '))

area2 = calculateTriangreArea(base, altura)
print("A área do triangulo 1 é ", area2)
'''