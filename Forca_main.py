import cabecario
import random
from random import choice

animais = ('ABELHA', 'BESOURO', 'CAVALO', 'DROMEDARIO', 'ELEFANTE', 'FALCAO', 'GORILA', 'HIPOPOTAMO', 'IGUANA',
           'JACARE', 'LEAO', 'MACACO', 'ONCA', 'PANTERA', 'RATO', 'SURICATE', 'TUCANO', 'URSO', 'VESPA')
animal_pc = random.choice(animais)  # animal aleatorio escolhido pelo computador
contagem_erros = 0
tracos = [' ━━ ']
letras_erradas = []

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
            dica()  # dica
            while True:  # enquanto o user digitar errado:
                try:
                    letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                except (ValueError, IndexError):
                    print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                else:
                    while True: # se nao der erro:
                        if letra_escolhida.isalpha() is False:
                            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                            letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                        else:
                            break
                    while True:
                        if letra_escolhida in tracos or letra_escolhida in letras_erradas:
                            print('\033[1;31mVOCÊ JA DIGITOU ESSA LETRA, PORFAVOR ESCOLHA OUTRA\033[m')
                            while True:  # enquanto o user digitar errado:
                                    try:
                                        letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                    except (ValueError, IndexError):
                                        print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                    else:
                                        break
                        else:
                            break

                    break
                    # usuario escolheu uma letra

            while True:  # enquanto a letra nao existir no animal faz isso...
                letras_erradas.append(letra_escolhida)
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
                            letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                        except (ValueError, IndexError):
                            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                        else:
                            while True:
                                if letra_escolhida.isalpha() is False: # se a letra escolhida nao for albatetica imprime mensagem de erro
                                    print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                    letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                else:
                                    break
                            while True:
                                if letra_escolhida in tracos or letra_escolhida in letras_erradas: # se o usuario ja estiver digitado a letra
                                    print('\033[1;31mVOCÊ JA DIGITOU ESSA LETRA, PORFAVOR ESCOLHA OUTRA\033[m')
                                    while True:  # enquanto o user digitar errado:
                                        try:
                                            letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                        except (ValueError, IndexError):
                                            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                        else:
                                            while True:
                                                if letra_escolhida.isalpha() is False:  # se a letra escolhida nao for albatetica imprime mensagem de erro
                                                    print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                                    letra_escolhida = str(
                                                        input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                                else:
                                                    break

                                            break
                                else:
                                    break

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
                            for c, valores in enumerate(animal_pc):   # PRA DESCOBRIR A POSIÇÃO QUE A LETRA ESTÁ E POR NA LISTA : CORRETA LETRAS
                                if valores == letra_escolhida:
                                    del tracos[c] # tira o traço da forca
                                    tracos.insert(c,valores) # coloca a letra no lugar do traço
                                    corretas_letras.append(c) # coloca a letra na lista letras corretas


                            if tracos.count(' ━━ ') == 0:
                                print('\033[1;32mVOCÊ VENCEU O JOGO, PARABÉNS\033[m')
                                print(f'\033[1;34mO ANIMAL É: {animal_pc.upper()}\033[m')
                                #print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')

                            else:
                                mostra_tracinho()




                        else:
                            break
                        if tracos.count(' ━━ ') != 0:
                            while True:  # enquanto o user digitar errado:
                                    try:
                                        letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                    except (ValueError, IndexError):
                                        print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                    else:
                                        while True:
                                            if letra_escolhida.isalpha() is False:
                                                print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                                letra_escolhida = str(
                                                    input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                            else:
                                                break
                                        break
                            while True:
                                if letra_escolhida in tracos or letra_escolhida in letras_erradas:
                                    print('\033[1;31mVOCÊ JA DIGITOU ESSA LETRA, PORFAVOR ESCOLHA OUTRA\033[m')
                                    while True:  # enquanto o user digitar errado:
                                        try:
                                            letra_escolhida = str(input('\033[1;32mESCOLHA SUA LETRA: \033[m')).upper()
                                        except (ValueError, IndexError):
                                            print('\033[1;31mERRO: Valor incorreto, tente denovo.\033[m')
                                        else:
                                            break

                                else:
                                    break
                            break
                elif tracos.count(' ━━ ') == 0:
                        print('\033[1;32mVOCÊ VENCEU O JOGO, PARABÉNS\033[m')
                        print(animal_pc)
                        break


            print('\n')
            print('☟'*23)
            cabecario.painel('DESEJA CONTINUAR?')
            cont_para1 = int(input('\033[97mSua opção:\033[m '))
            if cont_para1 == 2:
                print('\033[1;32mObrigado, volte sempre\033[m')
                break

        if contagem_erros == 6:
            print('\033[1;31mBOA SORTE NA PROXIMA VEZ\033[m')
            for c in animal_pc:
                c.replace(" ", "")
            print(animal_pc.replace(" ", "-"))
            break


        break

