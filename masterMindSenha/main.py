import random

def valida_senha(senha):
    global cores
    temp = []
    def a () :
        for i in senha:
            if i in cores and not(i in temp):
                temp.append(i)
                continue
            else:
                return False
        return True

    def tamanho() :
        if len(temp) == 4:
            return True
        else:
            return False
    if a() and tamanho() == True:
        return True
    else:
        return False

def retira_pino(senha):
    global pinos_verdes
    global pinos_amarelos
    global pinos_roxos
    global pinos_azuis
    global pinos_vermelhos
    global pinos_laranjados
    global tentativas

    cont = 0

    for i in senha:
        if i == 'amarelo':
            pinos_amarelos -= 1
            cont += 1
            continue
        elif i == 'verde':
            pinos_verdes -= 1
            cont += 1
            continue
        elif i == 'azul':
            pinos_azuis -= 1
            cont += 1
            continue
        elif i == 'roxo':
            pinos_roxos -= 1
            cont += 1
            continue
        elif i == 'vermelho':
            pinos_vermelhos -= 1
            cont += 1
            continue
        elif i == 'laranjado':
            pinos_laranjados -= 1
            cont += 1
            continue
    tentativas -= 1
    pass

def status_do_jogo():
    print('Você ainda tem:')
    print(pinos_azuis, 'pinos azuis,')
    print(pinos_roxos, 'pinos roxos,')
    print(pinos_verdes, 'pinos verdes,')
    print(pinos_laranjados, 'pinos laranjados,')
    print(pinos_amarelos, 'pinos amarelos,')
    print(pinos_vermelhos, 'pinos vermelhos e')
    print(tentativas, 'tentativas restante.\nBoa sorte!!!')

def escolha_senha_1():
    senha = input('\nSenha inválida! \nEscolha 4 cores dentre:\namarelo, verde, azul, roxo, vermelho, laranjado. \nAs cores não podem ser repetidas.\nDigite as cores separadas por"," e sem espaços.\n\nDigite a senha:').lower().split(',')
    return senha

def escolha_senha_2():
    senha = input('\nDigite outra senha!').lower().split(',')
    return senha

def retorno_da_senha():
    print('Esta foi a rua senha',senha)
    print('Este foi o seu retorno',aux)

def limpa_senha():
    global aux
    global senha
    del aux [:]
    del senha[:]

def ganhou (aux):
    branco = int(0)
    for i in aux:
        if i == 'branco':
            branco += 1
        continue
    if branco == 4:
        return True

def perdeu ():
    global pinos_verdes
    global pinos_amarelos
    global pinos_roxos
    global pinos_azuis
    global pinos_vermelhos
    global pinos_laranjados
    global tentativas
    global pino_cor

    quant_pino = int(0)
    if tentativas == 0:
        pino_cor = '\n\nSuas tentativas acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_verdes == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_amarelos == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_roxos == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_azuis == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_vermelhos == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    elif pinos_laranjados == 0:
        quant_pino += 1
        pino_cor = '\n\nSeus pinos acabaram!\nInfelizmente você perdeu!'
        return True
    else:
        return False

def reinicio ():
    global pinos_verdes
    global pinos_amarelos
    global pinos_roxos
    global pinos_azuis
    global pinos_vermelhos
    global pinos_laranjados
    global tentativas

    pinos_laranjados = 5
    pinos_vermelhos = 5
    pinos_verdes = 5
    pinos_azuis = 5
    pinos_roxos = 5
    pinos_amarelos = 5
    tentativas = 6


def nova_senha_aleatoria():
    global senha_aleatoria
    senha_aleatoria = random.sample(cores, 4)

cores = ['amarelo', 'verde', 'azul', 'roxo', 'vermelho', 'laranjado']
aux = []

pino_cor = str()
pino_preto = str('preto')
pino_vazio = str('vazio')
pino_branco = str('branco')

pinos_amarelos = int(5)
pinos_verdes = int(5)
pinos_azuis = int(5)
pinos_roxos = int(5)
pinos_vermelhos = int(5)
pinos_laranjados = int(5)

tentativas = int(6)


print(f'Este é o jogo da senha,é um jogo de adivinhação e, de certa forma, estratégia.\n'
       f'O programa sorteia uma sequência de 4 cores entre as 6 opções do jogo: \n'
       f'(amarelo, verde, azul, roxo, vermelho e laranjado) e o jogador deve tentar \n'
       f'adivinhar qual a sequência determinada.\n'
       f'Para que o jogador não apenas jogue cegamente sequências aleatórias de cores,\n'
       f'o jogo irá dar dicas sobre os “chutes”.\n'
       f'Isto é, ele usa pinos brancos e pretos para sinalizar quão perto a sequência\n'
       f'adivinhada está da sequência real, nestes 3 casos:\n'
       f'➔ Caso a cor corresponda à cor na exata posição chutada, utiliza-se o pino branco;\n'
       
       f'➔ Caso a cor corresponda à alguma cor da sequência, mas está na posição incorreta, utiliza-se o pino preto;\n'
       
       f'➔ Caso a cor não corresponda a nenhuma cor da sequência, deixa-se vazio.\n'
       
       f'É importante ressaltar que a senha gerada para ser adivinhada não tem nenhuma cor repetida e\n'
       f'não pode incluir os pinos brancos ou pretos, abrangendo apenas as 6 cores citadas anteriormente.\n'
       f'O jogador terá 5 pinos de cada cor e 6 tentativas, se acabarem os pinos ou as tentativas o jogo se encerra.\n')

comecar = input('Deseja jogar? (y/n):')

senha_aleatoria = random.sample(cores, 4)

if comecar == 'y':
    senha = escolha_senha_1()
    flag = True
    while(flag) :
        if valida_senha(senha):
            cont = int(0)
            for i in senha:
                if i == senha_aleatoria[cont]:
                    aux.append(pino_branco)
                    cont += 1
                    continue
                elif i in senha_aleatoria:
                    aux.append(pino_preto)
                    cont += 1
                    continue
                else:
                    aux.append(pino_vazio)
                    cont += 1
                    continue

            retira_pino(senha)
            status_do_jogo()
            retorno_da_senha()
            if ganhou(aux):
                print('\n<<<<Parabéns!!!>>>>\n<<<<Você ganhou!!!>>>>\n')
                temp = str(input('Deseja jogar novamente? (y/n):'))
                if temp == 'y':
                    reinicio()
                    limpa_senha()
                    nova_senha_aleatoria()
                    pass
                else:
                    flag = False
                    print('\nObrigado pela sua participação!')
                continue
            elif perdeu():
                print(pino_cor)
                temp = str(input('Deseja jogar novamente? (y/n):'))
                if temp == 'y':
                    reinicio()
                    limpa_senha()
                    nova_senha_aleatoria()
                    pass
                else:
                    flag = False
                    print('Obrigado pela sua participação!')
            else:
                limpa_senha()
                senha = escolha_senha_2()
            pass
        else:
            senha = escolha_senha_1()
            pass
else:
    pass

print('\nObrigado pela atenção!!!\nAté breve!!!\n\nBy Michael Douglas-MDSS!')
