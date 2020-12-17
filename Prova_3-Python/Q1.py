'''
[ Questão criada por Deyvid Gonçalves (adaptado)]
Faça um programa que faça pesquisa do produto de um supermercado, preço e a quantidade em estoque.
Para fazer esse programa use tupla e pelo menos duas funções. Para sair do programa será preciso digitar 0.
A tupla deve ter no mínimo 5 produtos. 
'''

produtos = ('xxxxx', 'Banana','Laranja', 'Melancia', 'Manga', 'Uva', 'Caju', 'Abacate')
quantidade = ('xxxxx', 50, 80, 13, 42, 30, 68, 28)
preço = ('xxxx',5, 1, 10, 3, 5, 2, 7)
continuaçao = True

def exibir(x, y):
    print(f'{x}\t {y[x]} ')

def verificar(x, y, z, p):
    print(f'Produto: {p[z]}')
    print(f'Quantidade em estoque: {x[z]}')
    print(f'Preço por unidade: R$ {y[z]}')

while continuaçao == True:
    print('CÓDIGO\tPRODUTOS')
    print('-=' * 30)

    for i in [1,2,3,4,5,6,7]:
        exibir(i, produtos)

    print('-=' * 30)

    pergunta = int(input('Digite o código que deseja verificar a quantidade e o preço: (para encerrar digite 0) '))

    if(pergunta == 0):
        print('Encerrando')
        break 
    elif(pergunta < 0) or (pergunta > 7):
        print('Invalido, tente novamente')
    else:
        verificar(quantidade, preço, pergunta, produtos)
