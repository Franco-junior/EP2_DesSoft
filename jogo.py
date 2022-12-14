#Aqui será implantado o código do jogo do EP2
from funcoes import *
from questoes import *
branco=('\033[0;30m')
vermelho=('\033[0;31m')
verde=('\033[0;32m')
amarelo=('\033[0;33m')
azulclaro=('\033[0;34m')
roxo=('\033[0;35m')
verdeagua=('\033[0;36m')
cinza=('\033[0;37m')
    
questoes_formatadas = transforma_base(lista)

print('Olá, seja bem-vindo(a) ao jogo {0}Fortuna DesSoft'.format(amarelo))
nome = input('{0}Digite seu nome: '. format(cinza))
print('Ok {0}, neste jogo você tem direito a 3 pulos e 2 ajudas para auxiliá-l@!'.format(nome))
print('{0}As suas opções de escolha são: "A", "B", "C", "D", "ajuda", "pular" e "parar"{1}\n'.format(verde, cinza))
print("Vamos começas com as questões do nivel FACIL")
come = input('Aperte ENTER para começar o jogo e boa sorte :)')
print(f"{cinza}")

operacao = True
acertos = 0
primeira = False
resppossiv = ['A', 'B', 'C', 'D', 'ajuda', 'pular', 'parar']
premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
lista_sorteada = []
ajudas = 2
pulos = 3
indquest = 1
while operacao:
    while acertos < 3:
        quest = sorteia_questao(questoes_formatadas, 'facil')
        if primeira == True:
            quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
        primeira = True
        quest_text = questao_para_texto(quest, indquest)
        print(quest_text)
        resposta = input('Resposta: ')
        if resposta == quest['correta']:
            acertos += 1
            print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
            indquest += 1
        elif resposta == 'ajuda':
            if ajudas <= 0:
                print('Infelizmente você não possui mais ajudas :(')
                resposta = input('Resposta: ')
                while resposta == 'ajuda':
                    print('Infelizmente você não possui mais ajudas :(')
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos > 0):
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos <= 0):
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
            else:
                print('Ok, ajuda à caminho...\n')
                ajudas -= 1
                print('Você possui {0} ajudas restantes...'.format(ajudas))
                print(gera_ajuda(quest))
                resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
                while resposta == 'ajuda':
                    print('Desculpe, você já pediu ajuda nessa questão!!')
                    resposta = input('Resposta: ')
                    if resposta == quest['correta']:
                        acertos += 1
                        print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                        indquest += 1
                if resposta == 'pular':
                    while pulos > 0:
                        print('OK, pulando questão...')
                        print('Você possui {0} pulos restantes...'.format(pulos))
                        quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                        quest_text = questao_para_texto(quest, indquest)
                        print(quest_text)
                        resposta = input('Resposta: ')
                        if resposta == quest['correta']:
                            acertos += 1
                            print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                            indquest += 1
        elif resposta == 'pular':
            while pulos < 0:
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
            if pulos == 0:
                print('Infelizmente você não tem mais pulos :(\n')
                resposta = input('Resposta: ')
                while resposta == 'pular':
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')

        elif resposta == 'parar':
            print('Ok, parando...')
            print('Parabéns, seu prêmio final é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
            acertos = 10
            operacao = False

        elif resposta not in resppossiv:
            print('{0}Opção inválida!!!{1}'.format(vermelho, cinza))
            print('Suas opções são: {0}"A", "B", "C", "D", "ajuda", "pular", "parar"{1}'. format(verde, cinza))
            resposta = input('Resposta: ')
        elif resposta != quest['correta']:
            print('Infelizmente você errou e não levará nada :(')
            acertos = 10
            operacao = False
    
    while 3 <= acertos < 6:
        if acertos == 3:
            print('Agora vamos para as questões médias...')
        quest = sorteia_questao(questoes_formatadas, 'medio')
        if primeira == True:
            quest = sorteia_questao_inedida(questoes_formatadas, 'medio', lista_sorteada)
        primeira = True
        quest_text = questao_para_texto(quest, indquest)
        print(quest_text)
        resposta = input('Resposta: ')
        if resposta == quest['correta']:
            acertos += 1
            print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
            indquest += 1
        elif resposta == 'ajuda':
            if ajudas <= 0:
                print('Infelizmente você não possui mais ajudas :(')
                resposta = input('Resposta: ')
                while resposta == 'ajuda':
                    print('Infelizmente você não possui mais ajudas :(')
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos > 0):
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos <= 0):
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
            else:
                print('Ok, ajuda à caminho...\n')
                ajudas -= 1
                print('Você possui {0} ajudas restantes...'.format(ajudas))
                print(gera_ajuda(quest))
                resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
                while resposta == 'ajuda':
                    print('Desculpe, você já pediu ajuda nessa questão!!')
                    resposta = input('Resposta: ')
                    if resposta == quest['correta']:
                        acertos += 1
                        print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                        indquest += 1
                if resposta == 'pular':
                    while pulos > 0:
                        print('OK, pulando questão...')
                        print('Você possui {0} pulos restantes...'.format(pulos))
                        quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                        quest_text = questao_para_texto(quest, indquest)
                        print(quest_text)
                        resposta = input('Resposta: ')
                        if resposta == quest['correta']:
                            acertos += 1
                            print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                            indquest += 1
        elif resposta == 'pular':
            while pulos < 0:
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
            if pulos == 0:
                print('Infelizmente você não tem mais pulos :(\n')
                resposta = input('Resposta: ')
                while resposta == 'pular':
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')

        elif resposta == 'parar':
            print('Ok, parando...')
            print('Parabéns, seu prêmio final é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
            acertos = 10
            operacao = False

        elif resposta not in resppossiv:
            print('{0}Opção inválida!!!{1}'.format(vermelho, cinza))
            print('Suas opções são: {0}"A", "B", "C", "D", "ajuda", "pular", "parar"{1}'. format(verde, cinza))
            resposta = input('Resposta: ')
        elif resposta != quest['correta']:
            print('Infelizmente você errou e não levará nada :(')
            acertos = 10
            operacao = False
      
    while 6 <= acertos < 9:
        if acertos == 6:
            print('Agora vamos para as questões difíceis...')
        quest = sorteia_questao(questoes_formatadas, 'dificil')
        if primeira == True:
            quest = sorteia_questao_inedida(questoes_formatadas, 'dificil', lista_sorteada)
        primeira = True
        quest_text = questao_para_texto(quest, indquest)
        print(quest_text)
        resposta = input('Resposta: ')
        if resposta == quest['correta']:
            acertos += 1
            if acertos == 9:
                print('Parabéns, você venceu o jogo e ganhou o prêmio final de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                perguntafinal = input('Deseja jogar novamente? [S/N]')
                if perguntafinal == 'S':
                    acertos = 0
                    ajudas = 2
                    pulos = 3
                    primeira = False
                    lista_sorteada.clear()
                    indquest = 1
            else:
                print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                indquest += 1

        elif resposta == 'ajuda':
            if ajudas <= 0:
                print('Infelizmente você não possui mais ajudas :(')
                resposta = input('Resposta: ')
                while resposta == 'ajuda':
                    print('Infelizmente você não possui mais ajudas :(')
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos > 0):
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
                while (resposta == 'pular') and (pulos <= 0):
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
            else:
                print('Ok, ajuda à caminho...\n')
                ajudas -= 1
                print('Você possui {0} ajudas restantes...'.format(ajudas))
                print(gera_ajuda(quest))
                resposta = input('Resposta: ')
                if resposta == quest['correta']:
                    acertos += 1
                    print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                    indquest += 1
                while resposta == 'ajuda':
                    print('Desculpe, você já pediu ajuda nessa questão!!')
                    resposta = input('Resposta: ')
                    if resposta == quest['correta']:
                        acertos += 1
                        print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                        indquest += 1
                if resposta == 'pular':
                    while pulos > 0:
                        print('OK, pulando questão...')
                        print('Você possui {0} pulos restantes...'.format(pulos))
                        quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                        quest_text = questao_para_texto(quest, indquest)
                        print(quest_text)
                        resposta = input('Resposta: ')
                        if resposta == quest['correta']:
                            acertos += 1
                            print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
                            indquest += 1
        elif resposta == 'pular':
            while pulos < 0:
                    print('OK, pulando questão...')
                    quest = sorteia_questao_inedida(questoes_formatadas, 'facil', lista_sorteada)
                    quest_text = questao_para_texto(quest, indquest)
                    print(quest_text)
                    resposta = input('Resposta: ')
            if pulos == 0:
                print('Infelizmente você não tem mais pulos :(\n')
                resposta = input('Resposta: ')
                while resposta == 'pular':
                    print('Infelizmente você não tem mais pulos :(\n')
                    resposta = input('Resposta: ')

        elif resposta == 'parar':
            print('Ok, parando...')
            print('Parabéns, seu prêmio final é de R$ {0}{1:.2f}{2}\n'.format(verde, premios[acertos-1], cinza))
            acertos = 10
            operacao = False

        elif resposta not in resppossiv:
            print('{0}Opção inválida!!!{1}'.format(vermelho, cinza))
            print('Suas opções são: {0}"A", "B", "C", "D", "ajuda", "pular", "parar"{1}'. format(verde, cinza))
            resposta = input('Resposta: ')
        elif resposta != quest['correta']:
            print('Infelizmente você errou e não levará nada :(')
            acertos = 10
            operacao = False
