'''
[Questão criada por Willemberg Bruno (adaptada)]
Faça um sistema de cadastro de entrada dos pacientes no hospital, utilizando dicionário guarde as informações do nome,
o estado do paciente é (Leve, Grave ou Critico). Se o paciente estiver em estado leve receberá a pulseira verde,
se estiver em estado grave receberá a pulseira amarela e em estado crítico receberá a pulseira vermelha,
por fim exiba todos os pacientes cadastrados, o seu estado e qual pulseira ele receberá. Para seu programa use pelo menos duas funções.
'''

import os

nome_estado = {}
pulseira = []

def funcEstado(x):
    if x == 'LEVE':
        pulseira.append('VERDE')
    elif x == 'GRAVE':
        pulseira.append('AMARELA')
    elif x == 'CRITICO':
        pulseira.append('VERMELHA')

for i in range(5):
    nome = str(input('Qual o nome do paciente? '))
    nome = nome.upper()
    estado = str(input('Qual o estado de {nome} {Leve, Grave ou Critico}? '))
    estado = estado.upper()
    nome_estado[nome] = (estado)
    funcEstado(estado)
    os.system("cls")

def exibir(x, s, p):
    for k,v in nome_estado.items():
        print(f'Paciente: {k}')
        print(f'Estado: {v}')
        print(f'Pulseira: {p[x]}')
        x += 1
        print('-=' * s)

z = 0
print(exibir(z, 20, pulseira))
