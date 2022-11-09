with open('questoes.py', 'r') as arquivo:
    questoes = arquivo.read()

def valida_questao(questao):
    print(questao)
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

def transforma_base (questoes):
    if questoes == []:
        return {} 
    facil = []
    medio = []
    dificil = []
    dici = {}
    for i in range(len(questoes)):
        nivel = questoes[i]['nivel']
        if nivel == 'facil':
            facil.append(questoes[i])
        elif nivel == 'medio':
            medio.append(questoes[i])
        elif nivel == 'dificil':
            dificil.append(questoes[i])
    if facil != []:
        dici['facil'] = facil
    if medio != []:
        dici['medio'] = medio
    if dificil != []:
        dici['dificil'] = dificil
    return dici

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
    print(questao)
    print(id)
    lista_op = questao['opcoes']
    a = lista_op['A']
    b = lista_op['B']
    c = lista_op['C']
    d = lista_op['D']
    resultado = ('----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}'.format(id, questao['titulo'], a, b, c, d))
    return resultado

def gera_ajuda (questao):
    print(questao)
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
        return resultado