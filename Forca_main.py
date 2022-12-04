import cabecario
import random
from random import choice

animais = ('abelha', 'besouro', 'cavalo', 'dromedario', 'elefante', 'falcao', 'gorila', 'hipopotamo', 'iguana',
           'jacare', 'leao', 'macaco', 'onca', 'pantera', 'rato', 'suricate', 'tucano', 'urso', 'vespa')
animal_pc = random.choice(animais)  # animal aleatorio escolhido pelo computador
contagem_erros = 0
tracos = [' ━━ ']

def mostra_tracinho():
    for c in tracos:
        print(c, end=' ')  # mostrando as linhas
    print()


def dica():
    print('                 \033[1;40;33mDICA: ANIMAIS \033[m')


while True:
    cabecario.painel('BEM-VINDO AO JOGO DA FORCA')
    while True:  # se o usuario digitar uma opção invalida
        try:
            cont_para = int(input('\033[97mSua opção:\033[m '))
        except (ValueError,IndexError):
            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
        else:
            break
    if cont_para == 2:
        print('\033[1;32mObrigado, volte sempre\033[m')
        break
    if cont_para == 1:
        while True:
            animal_pc = random.choice(animais)  # escolha do animal
            tracos = [] # lista com os tracinhos
            for c in animal_pc:
                tracos.append(' ━━ ')
            cabecario.mostra_forca_0()
            mostra_tracinho() # mostra so tracejados
            #print('━━━ ' * len(animal_pc))  # mostrando a linha pra conter as letras
            dica()  # dica
            while True:  # enquanto o user digitar errado:
                try:
                    letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).lower()
                except (ValueError, IndexError):
                    print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                else:
                    break
                    # usuario escolheu uma letra

            while True:  # enquanto a letra nao existir no animal faz isso...
                if tracos.count(' ━━ ') == 0:
                    break

                if letra_escolhida not in animal_pc:
                    contagem_erros += 1  # mais um erro
                    if contagem_erros == 1:
                        cabecario.mostra_forca_1()  # mostra a forca 1
                    elif contagem_erros == 2:
                        cabecario.mostra_forca_2()  # mostra a forca 2
                    elif contagem_erros == 3:
                        cabecario.mostra_forca_3()  # mostra a forca 3
                    elif contagem_erros == 4:
                        cabecario.mostra_forca_4()  # mostra a forca 4
                    elif contagem_erros == 5:
                        cabecario.mostra_forca_5()  # mostra a forca 5
                    elif contagem_erros == 6:
                        cabecario.mostra_forca_6()  # mostra a forca 6
                        break

                    mostra_tracinho()
                    print('\033[1;31mQUE PENA, A LETRA NAO EXISTE NESTE ANIMAL\033[m')

                    while True:  # enquanto o user digitar errado:
                        try:
                            letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).lower()
                        except (ValueError, IndexError):
                            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                        else:
                            break
                if letra_escolhida in animal_pc:
                    while True:
                        if tracos.count(' ━━ ') == 0:
                            break
                        if contagem_erros == 0:
                            cabecario.mostra_forca_0()  # mostra a forca 1
                        if contagem_erros == 1:
                            cabecario.mostra_forca_1()  # mostra a forca 1
                        elif contagem_erros == 2:
                            cabecario.mostra_forca_2()  # mostra a forca 2
                        elif contagem_erros == 3:
                            cabecario.mostra_forca_3()  # mostra a forca 3
                        elif contagem_erros == 4:
                            cabecario.mostra_forca_4()  # mostra a forca 4
                        elif contagem_erros == 5:
                            cabecario.mostra_forca_5()  # mostra a forca 5
                        elif contagem_erros == 6:
                            cabecario.mostra_forca_6()  # mostra a forca 6
                            break



                        #mostra_tracinho()

                        if letra_escolhida in animal_pc:        # se a letra tiver no animal
                            corretas_letras = []    # cria uma lista com as letras
                            for c, valores in enumerate(animal_pc):   # PRA DESCOBRIR A POSIÇÃO QUE A LETRA TA E POR NA LISTA CORRETA LETRAS
                                if valores == letra_escolhida:
                                    del tracos[c] # tira o traço
                                    tracos.insert(c,valores) # coloca a letra no lugar do traço
                                    corretas_letras.append(c) # coloca a letra na lista letras corretas
                                    if tracos.count(' ━━ ') == 0:
                                        print('\033[1;32mVOCÊ VENCEU O JOGO, PARABÉNS\033[m')
                                        break


                            mostra_tracinho()

                        else:
                            break
                        if tracos.count(' ━━ ') != 0:
                            while True:  # enquanto o user digitar errado:
                                    try:
                                        letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).lower()
                                    except (ValueError, IndexError):
                                        print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                    else:
                                        break
                elif tracos.count(' ━━ ') == 0:
                        print('\033[1;32mVOCÊ VENCEU O JOGO, PARABÉNS\033[m')
                        break
            break

        if contagem_erros == 6:
            print('\033[1;31mBOA SORTE NA PROXIMA VEZ\033[m')
            break


        break

# erros a serem melhorados: se o usuario digitar a mesma letra, se o usuario nao digitar nada