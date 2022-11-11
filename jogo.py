#Aqui será implantado o código do jogo do EP2

branco=('\033[0;30m')
vermelho=('\033[0;31m')
verde=('\033[0;32m')
amarelo=('\033[0;33m')
azulclaro=('\033[0;34m')
roxo=('\033[0;35m')
verdeagua=('\033[0;36m')
cinza=('\033[0;37m')

print('Olá, seja bem-vindo(a) ao jogo {0}Fortuna DesSoft'.format(amarelo))
nome = input('{0}Digite seu nome: '. format(cinza))
print('{0}, neste jogo você tem direito a 3 pulos e 2 ajudas para auxiliar'.format(nome))
print('{0}As suas opções de escolha são: "A", "B", "C", "D", "ajuda", "pula" e "parar"\n'.format(verde))
come = input('Aperte ENTER para começar o jogo e boa sorte :)')
