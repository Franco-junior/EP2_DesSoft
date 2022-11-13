#Aqui será implantado o código do jogo do EP2

branco=('\033[0;30m')
vermelho=('\033[0;31m')
verde=('\033[0;32m')
amarelo=('\033[0;33m')
azulclaro=('\033[0;34m')
roxo=('\033[0;35m')
verdeagua=('\033[0;36m')
cinza=('\033[0;37m')

listaa = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},
         
         {'titulo': 'Que substância é absorvida pelas plantas e expirada pelo ser humano?',
          'nivel': 'facil',
          'opcoes': {'A': 'Oxigênio', 'B': 'Nitrogênio', 'C': 'Dióxido de carbono', 'D': 'Monóxido de carbono'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 181 - 72?',
          'nivel': 'facil',
          'opcoes': {'A': '101', 'B': '109', 'C': '107', 'D': '105'},
          'correta': 'B'},
         
         {'titulo': 'O que é Via Láctea?',
          'nivel': 'facil',
          'opcoes': {'A': 'Marca de leite', 'B': 'Civilização antiga', 'C': 'Galáxia', 'D': 'Carro'},
          'correta': 'C'},

         {'titulo': 'Quais o menor e maior país do mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Vaticano e Rússia', 'B': 'Mônaco e Canadá', 'C': 'Malta e Estados Unidos', 'D': 'São Marino e China'},
          'correta': 'A'},
         
         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},
         
         {'titulo': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
          'nivel': 'facil',
          'opcoes': {'A': 'Asterístico, exceção, meteorologia, entertido', 'B': 'Asterisco, exceção, meteorologia, entretido', 'C': 'Asterisco, excessão, metereologia, entretido', 'D': 'Asterístico, excessão, metereologia, entertido'},
          'correta': 'B'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},
         
         {'titulo': 'Qual montanha se localiza entre a fronteira do Tibet com o Nepal?',
          'nivel': 'facil',
          'opcoes': {'A': 'Monte Fuji', 'B': 'Monte Verde', 'C': 'Monte Carlo', 'D': 'Monte Everest'},
          'correta': 'D'},

         {'titulo': '___ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},
         
         {'titulo': 'Qual é o nome que descobriu o processo de pasteurização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Antoine Lavoisier', 'B': 'Louis Pasteur', 'C': 'Charles Darwin', 'D': 'Marie Curie'},
          'correta': 'B'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Que país da Europa é conhecido como Países Baixos?',
          'nivel': 'medio',
          'opcoes': {'A': 'Holanda', 'B': 'Áustria', 'C': 'Bélgica', 'D': 'Inglaterra'},
          'correta': 'A'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},
         
         {'titulo': 'Quem pintou "Guernica"?',
          'nivel': 'medio',
          'opcoes': {'A': 'Paul Cézanne', 'B': 'Salvador Dalí', 'C': 'Pablo Picasso', 'D': 'Tarsila do Amaral'},
          'correta': 'C'},
         
         {'titulo': 'As pessoas de qual tipo sanguíneo são consideradas doadoras universais?',
          'nivel': 'medio',
          'opcoes': {'A': 'Tipo A', 'B': 'Tipo B', 'C': 'Tipo O', 'D': 'TIpo ABO'},
          'correta': 'C'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de ___, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},
         
         {'titulo': 'Como faço para chamar o telefone de emergência nos EUA?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 191', 'B': 'Ligue 192', 'C': 'Ligue 910', 'D': 'Ligue 911'},
          'correta': 'D'},
         
         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},
         
         {'titulo': 'Qual a pessoa mais seguida no Facebook?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Lionel Messi', 'C': 'Neymar Jr.', 'D': 'Pelé'},
          'correta': 'A'},

         {'titulo': 'Que profissional usa uma ferramenta chamada formão?',
          'nivel': 'medio',
          'opcoes': {'A': 'Confeiteiro', 'B': 'Bombeiro', 'C': 'Carpinteiro', 'D': 'Relojoeiro'},
          'correta': 'C'},
         
         {'titulo': 'Como se chama o estudo entre palavras e signficados?',
          'nivel': 'medio',
          'opcoes': {'A': 'Fonética', 'B': 'Semântica', 'C': 'Filosofia', 'D': 'Psiquiatria'},
          'correta': 'B'},
         
         {'titulo': 'Qual era a nacionalidade do escritor Oscar Wilde?',
          'nivel': 'medio',
          'opcoes': {'A': 'Americano', 'B': 'Escocês', 'C': 'Irlandês', 'D': 'Inglês'},
          'correta': 'C'},
         
         {'titulo': 'Qual era o nome de Aleijadinho?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Alexandrino Francisco Lisboa', 'B': 'Manuel Francisco Lisboa', 'C': 'Alex Francisco Lisboa', 'D': 'Francisco Antônio Lisboa'},
          'correta': 'A'},
         
         {'titulo': '___ publicou o livro "O Prícipe" em __.',
          'nivel': 'dificil',
          'opcoes': {'A': 'Maquiavel, 1953', 'B': 'Thomas Hobbes, 1950', 'C': 'Maquiavel, 1951', 'D': 'Thomas Hobbes, 1952'},
          'correta': 'A'},
         
         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},
         
         {'titulo': 'Em que ano faleceu Charles Darwin?',
          'nivel': 'dificil',
          'opcoes': {'A': '1882', 'B': '1883', 'C': '1881', 'D': '1880'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},
         
         {'titulo': 'Em que ordem surgiram os modelos atômicos?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Thomson, Rutherford-Bohr, Dalton, Rutherford', 'B': 'Dalton, Thomson, Rutherford-Bohr, Rutherford', 'C': 'Thomson, Rutherford, Dalton, Rutherford-Bohr', 'D': 'Dalton, Thomson, Rutherford, Rutherford-Bohr'},
          'correta': 'D'},
         
         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},
         
         {'titulo': 'Qual a montanha mais alta do Brasil e com quantos metros de altitude?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Pico da Bandeira, com 2891,32 metros de altitude', 'B': 'Pico da Neblina, com 2995,30 metros de altitude', 'C': 'Pico da Bandeira, com 2789,45 metros de altitude', 'D': 'Pico da Neblina, com 2 792,82 metros de altitude'},
          'correta': 'B'}
        ]
    
def valida_questao(questao):
        titulo_validez = True
        nivel_validez = True
        opcoes_validez = True
        correta_validez = True
        validez = True
        retorno = {}
        #Chaves estão na questão?
        if 'titulo' not in questao:
            retorno['titulo'] = 'nao_encontrado'
            titulo_validez = False
            validez = False
        if 'nivel' not in questao:
            retorno['nivel'] = 'nao_encontrado'
            nivel_validez = False
            validez =  False
        if 'opcoes' not in questao:
            retorno['opcoes'] = 'nao_encontrado'
            opcoes_validez = False
            validez = False
        if 'correta' not in questao:
            retorno['correta'] = 'nao_encontrado'
            correta_validez = False
            validez = False   
        #Questão tem exatamente quatro chaves?
        x = len(questao.keys())
        if x != 4:
            retorno['outro'] ='numero_chaves_invalido'
            validez = False 
        #Título está vazio ou contém apenas espaços/caracteres em branco?
        if titulo_validez == True:
            if questao['titulo'].strip() == '':
                retorno['titulo'] = 'vazio'
                validez = False
        if nivel_validez == True:
            if questao['nivel'].strip() == '':
                retorno['nivel'] = 'vazio'
                validez = False
        if opcoes_validez == True:
            if questao['opcoes'] == {}:
                retorno['opcoes'] = 'vazio'
                validez = False
        if correta_validez == True:
            if questao['correta'].strip() == '':
                retorno['correta'] = 'vazio'
                validez = False 
        #Nível contém um dos valores fácil, médio ou difícil?
        niveis = ['facil', 'medio', 'dificil']
        if nivel_validez == True:
            if questao['nivel'] not in niveis:
                retorno['nivel'] = 'valor_errado'
                validez = False  
        #O valor da chave opções tem exatamente quatro chaves?
        if opcoes_validez == True:
            opcoes = questao['opcoes']
            y = len(questao['opcoes'].keys())
            if y != 4:
                retorno['opcoes'] = 'tamanho_invalido'
                validez = False      
            #Todas as opções A, B, C e D existem?
            else:
                if 'A' not in opcoes:
                    questao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    validez = False
                elif 'B' not in opcoes:
                    questao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    validez = False
                elif 'C' not in opcoes:
                    questao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    validez = False
                elif 'D' not in opcoes:
                    questao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    validez = False
                opcoes_invalidas = {}
                #Alguma das opções A, B, C ou D está vazia ou contém apenas espaços/caracteres em branco?
                if opcoes['A'].strip() == '':
                    opcoes_invalidas['A'] = 'vazia'
                    validez = False
                if opcoes['B'].strip() == '':
                    opcoes_invalidas['B'] = 'vazia'
                    validez = False
                if opcoes['C'].strip() == '':
                    opcoes_invalidas['C'] = 'vazia'
                    validez = False
                if opcoes['D'].strip() == '':
                    opcoes_invalidas['D'] = 'vazia'
                    validez = False
                if opcoes_invalidas != {}:
                    retorno['opcoes'] = opcoes_invalidas
        #A resposta correta está definida como A, B, C ou D?
        respostas = ['A', 'B', 'C', 'D']
        if correta_validez == True:
            if questao['correta'] not in respostas:
                retorno['correta'] = 'valor_errado'
                validez = False
        #parte final do código que retorna os erros ou vazio
        if validez == True:
            return {}
        elif validez == False:
            return retorno

def valida_questoes(questoes):
        new_lista = []
        for i in range(len(questoes)):
            new_lista.append(valida_questao(questoes[i]))
        return new_lista

validezz = valida_questoes(listaa)

if {} in validezz:























import random
def sorteia_questao(dici, nivel_sel):
    lista_quest = dici[nivel_sel]
    questao = random.choice(lista_quest)
    return questao

def sorteia_questao_inedida(dici, quest_nivel, quest_sort):
    lista_quest = dici[quest_nivel]
    questao = sorteia_questao(dici, quest_nivel)
    while questao in quest_sort:
        questao = random.choice(lista_quest)
        if questao not in quest_sort:
            quest_sort.append(questao)
            return questao
    if questao not in quest_sort:
        quest_sort.append(questao)
        return questao

def questao_para_texto(questao, id):
    lista_op = questao['opcoes']
    a = lista_op['A']
    b = lista_op['B']
    c = lista_op['C']
    d = lista_op['D']
    resultado = ('----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}'.format(id, questao['titulo'], a, b, c, d))
    return resultado

def gera_ajuda (questao):
    resposta_correta = questao['correta']
    respostas = {}
    respostas.update(questao['opcoes'])
    del respostas[resposta_correta]
    vezes = random.randint(1,2)
    if vezes == 1:
        resposta_errada = random.choice(list(respostas.items()))
        resultado = 'DICA:\nOpções certamente erradas: {0}'.format(respostas[resposta_errada[0]])
        return resultado
    if vezes == 2:
        resposta_errada1 = random.choice(list(respostas.items()))
        new_respostas = {}
        new_respostas.update(respostas)
        del new_respostas[resposta_errada1[0]]
        resposta_errada2 = random.choice(list(new_respostas.items()))
        resultado = 'DICA:\nOpções certamente erradas: {0} | {1}'.format(respostas[resposta_errada1[0]], respostas[resposta_errada2[0]])
        return 

print('Olá, seja bem-vindo(a) ao jogo {0}Fortuna DesSoft'.format(amarelo))
nome = input('{0}Digite seu nome: '. format(cinza))
print('{0}, neste jogo você tem direito a 3 pulos e 2 ajudas para auxiliar'.format(nome))
print('{0}As suas opções de escolha são: "A", "B", "C", "D", "ajuda", "pula" e "parar"\n'.format(verde))
come = input('Aperte ENTER para começar o jogo e boa sorte :)')


