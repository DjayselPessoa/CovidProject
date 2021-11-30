from CONTROLLER.controlCore import ObjControlCore
from DATA.eRD import ObjExtractRotaDados
#  from pathlib import Path
import time
import os


active = True
while active:
    try:
        #  ------------------------------------------------
        os.chdir(os.path.dirname(__file__))
        pegarDirRaiz = str(os.getcwd())
        #  print("Ok1 ", pegarDirRaiz)
        #  print('- Verificando existência do arquivo -')
        exist = ObjExtractRotaDados.caminho(pegarDirRaiz)
        #  ------------------------------------------------
        if(exist is True):
            # time.sleep(2)
            # print('- O arquivo existe -')
            # time.sleep(1)
            # print('-'*50)
            print('-'*50)
            print(' '*16 + 'EXPERIMENTO COVID' + ' '*16)
            print('-'*50)
            time.sleep(1)
            escolha = str(input('Escolha uma das opções abaixo: \n\n| 0 |\n| 1 |\n| 2 |\n| 3 |\n| 4 |\n| 5 para SAIR |\n\n: ->'))
            # print(escolha, type(escolha))
            if(escolha not in '012345'):
                time.sleep(1)
                raise ValueError("- UTILIZE SOMENTE NÚMEROS -")
            if(escolha == '5'):
                time.sleep(1)
                print('Finalizando aplicação!')
                time.sleep(1)
                active = False
                continue
            if(escolha == '0'):
                active = ObjControlCore.control(escolha, pegarDirRaiz)
                continue
            elif(escolha == '1'):
                active = ObjControlCore.control(escolha, pegarDirRaiz)
                continue
            elif(escolha == '2'):
                active = ObjControlCore.control(escolha, pegarDirRaiz)
                continue
            elif(escolha == '3'):
                active = ObjControlCore.control(escolha, pegarDirRaiz)
                continue
            elif(escolha == '4'):
                active = ObjControlCore.control(escolha, pegarDirRaiz)
                continue
        else:
            print('O arquivo pode estar danificado -')
            continue
    except ValueError as e:
        print('-'*50 + "\nLOG: -> ", e)
        print('-'*50)
        time.sleep(1)
        continue
