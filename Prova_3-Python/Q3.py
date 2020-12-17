'''
[Questão criada por Myllena Laís (adaptada)]
Um aluno deseja saber suas médias antes da postagem de seu professor para planejar com antecedência as suas férias.
O aluno deseja criar um sistema que receba os nomes das disciplinas ( no mínimo 5) e as médias.
Se o aluno tiver média maior ou igual a 7 o aluno em todas as matérias cadastradas ele está de férias. 
Se alguma média for menor que 7 ele não estará de férias. Use lista e função padrão para criar seu programa. 
O seu programa deve mostrar a situação do aluno como resultando, exibindo se ele está de férias ou não.
'''

materia = []
media = []
cont = 0

for i in range(5):
    materia.append(str(input(f'Informe a matéria {i+1}: ')))

for i in range(len(materia)):
    media.append(float(input(f'Qual a sua média em {materia[i]}? ')))

for i in range(len(media)):
    if media[i] < 7 :
        cont += 1

def veri(x):
    if x >= 1:
        print(f'Você não está de férias, ficou em {x}')
    else:
        print('Parabéns! Você está de férias!')

veri(cont)