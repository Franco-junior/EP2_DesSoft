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
print('{0}As suas opções de escolha são: "A", "B", "C", "D", "ajuda", "pula" e "parar"{1}\n'.format(verde, cinza))
print("Vamos começas com as questões do nivel FACIL")
come = input('Aperte ENTER para começar o jogo e boa sorte :)')
print(f"{cinza}")

operacao = True
acertos = 0
premio = 0
primeira = False
resppossiv = ['A', 'B', 'C', 'D', 'ajuda', 'pular', 'parar']
lista_sorteada = []
ajudas = 2
pulos = 3
indquest = 1
while operacao:
    while programa:
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
            if acertos == 1:
                premio += 1000
                print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premio, cinza))
            elif acertos == 2:
                premio += 4000
                print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premio, cinza))
            elif acertos == 3:
                premio += 5000
                print('VOCÊ ACERTOU, seu prêmio agora é de R$ {0}{1:.2f}{2}\n'.format(verde, premio, cinza))
        elif resposta == 'ajuda':
                if ajudas == 0:
                    print('Infelizmente você não possui mais ajudas :(')
                else:    
                    ajudas -= 1
                    if ajudas > 0:
                        print("OK, lá vem ajuda! ATENÇÃO: Você só tem direito a mais {0} ajudas".format(ajudas))
                        print(gera_ajuda(quest))
                        resposta = input('Qual a sua resposta?! ')
                        while resposta not in resppossiv:
                            print("{0}Opção INVÁLIDA!".format(vermelho))
                            print("{0}As opções de resposta são A, B, C, D, pular e parar!{1}".format(azulclaro, cinza))
                            resposta = input("Qual a sua resposta? ")
                    if resposta == quest['correta']:
                        acertos += 1
                        premio += 1000
                        print('VOCÊ ACERTOU, seu prêmio agora é de {0}{1}{2}\n'.format(verde, premio, cinza))
                        pergunta = input('Aperte ENTER para continuar')
                    elif resposta == 'ajuda':
                        print("{0}Não deu! Você já pediu ajuda nessa questão!{1}".format(vermelho, cinza))
                    else:
                        print("{0}Que pena! Você errou e vai sair sem nada{1}".format(vermelho, cinza))
                        operacao = False
                        programa = False
        elif resposta == 'pula':
                if pulos != 0:
                    print('Pulando questão... ATENÇÃO: Você só tem direito a {} pulos'.format(pulos))
                quest = sorteia_questao_inedida()
                programa = False
                operacao = False
        elif resposta == 'parar':
                cert = input("Deseja mesmo parar[S/N]? ")
                while cert not in 'SN':
                    print("{0}Opção INVÁLIDA{1}".format(vermelho, cinza))
                    cert = input("Deseja mesmo parar[S/N]?")
                if cert == "S" and acertos != 0:
                    programa = False
                    operacao = False
                    print(f"Ok! Você parou e seu prêmio é de R$ {premio:.2f}")
                elif cert == "S" and acertos == 0:
                    print("Ok! Você parou mas, infelizmente, saiu sem nada :(")
                else:
                    print(quest_text)
                    resposta = input('Qual a sua resposta? ')
        else:
                print("{0}Que pena! Você errou e vai sair sem nada{1}".format(vermelho, cinza))
                operacao = False
                programa = False
