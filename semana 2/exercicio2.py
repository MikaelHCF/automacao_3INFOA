'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''
nf = int(input("Quantidades de falta :"))
nn = int(input("Nota do aluno :"))

if nn > 6 and nf >= 75:
    print("Aprovado")
else:
    print("Reprovado")