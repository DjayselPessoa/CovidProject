from pathlib import Path
from SCRIPTS.MATH.rd3Calc import ObjCalc
import time


class extractRotaDados:

    def caminho(self, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            pathTratado = str(self.pegarDirRaiz)
            home = Path(pathTratado)
            sourcePath = Path(home, "DATA", "dados.txt")
            # print(sourcePath)
            # print('ok2')
            arquivo = open(sourcePath, 'r+', encoding='utf8')
            # print('ok22')
            # print('ok3', qtd)
            # for linha in arquivo:
            #     print(linha)
            arquivo.close()
            # print(sourcePath)
            exist = True
            return exist

        except:
            print('Arquivo não encontrado!')
            exist = False
            return exist

    def extract(self, escolha, pegarDirRaiz):
        self.escolha = escolha
        # print(self.escolha, type(self.escolha), 'okok')
        self.pegarDirRaiz = pegarDirRaiz
        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "DATA", "dados.txt")
        arquivo = open(sourcePath, 'r+', encoding='utf8')
        qtd = int(arquivo.readline())
        arquivoLido = arquivo.readlines()[0:qtd]
        arquivo.close()
        # print(arquivoLido)
        # for linha in arquivoLido:
        #     print(linha)
        if(self.escolha == '0'):
            femQtd = 0
            masQtd = 0
            for i in arquivoLido:
                if(i[0] == 'F'):
                    femQtd += 1
                else:
                    masQtd += 1

            femQtdFim = ObjCalc.regrad3(femQtd, qtd)
            masQtdFim = ObjCalc.regrad3(masQtd, qtd)
            time.sleep(1)
            print(f'\n\nPorcentagem de participantes por gênero: \n\n| F | -> {femQtdFim}%\n| M | -> {masQtdFim}%\n\n')
            time.sleep(1)
            active = True
            return active

        if(self.escolha == '1'):
            femQtd = 0
            masQtd = 0
            femQtdV = 0
            masQtdV = 0
            femQtdP = 0
            masQtdP = 0
            qtdJovem = 0
            qtdAdulto = 0
            qtdIdoso = 0
            contraiuSim = 0
            contraiuNao = 0
            for linha in arquivoLido:
                i = linha.split(',')
                # print(i)

                if(i[0] == 'F'):
                    if(i[2] == 'V'):
                        femQtdV += 1
                    if(i[2] == 'P'):
                        femQtdP += 1
                    femQtd += 1
                else:
                    if(i[2] == 'V'):
                        masQtdV += 1
                    if(i[2] == 'P'):
                        masQtdP += 1
                    masQtd += 1
                if(0 <= int(i[1]) <= 19):
                    qtdJovem += 1
                elif(20 <= int(i[1]) <= 59):
                    qtdAdulto += 1
                elif(60 <= int(i[1])):
                    qtdIdoso += 1

                # feio demais mas funcionou
                if(i[3] == 'N\n'):
                    contraiuNao += 1
                elif(i[3] == 'S\n'):
                    contraiuSim += 1

            femTQtdFim = ObjCalc.regrad3(femQtd, qtd) # quantidade total final de mulheres na pesquisa
            masTQtdFim = ObjCalc.regrad3(masQtd, qtd) # quantidade total final de homens na pesquisa
            # femQtdVFim = ObjCalc.regrad3(femQtdV, femQtd) # quantidade de mulheres vacinadas entre as mulheres
            # femQtdPFim = ObjCalc.regrad3(femQtdP, femQtd) # quantidade de mulheres placebo entre as mulheres
            # masQtdVFim = ObjCalc.regrad3(masQtdV, masQtd) # quantidade de homens vacinadas entre as homens
            # masQtdPFim = ObjCalc.regrad3(masQtdP, masQtd) # quantidade de homens placebo entre as homens
            vacinados = femQtdV + masQtdV
            vacinadosFim = ObjCalc.regrad3(vacinados, qtd) # quantidade de vacinados no total
            placebo = femQtdP + masQtdP
            placeboFim = ObjCalc.regrad3(placebo, qtd) # quantidade de não vacinados no total
            contraiuSimFim = ObjCalc.regrad3(contraiuSim, qtd) # quantidade de infectados
            contraiuNaoFim = ObjCalc.regrad3(contraiuNao, qtd) # quantidade de não infectados
            jovemQtdFim = ObjCalc.regrad3(qtdJovem, qtd) # quantidade de jovens
            adultoQtdFim = ObjCalc.regrad3(qtdAdulto, qtd) # quantidade de adultos
            idosoQtdFim = ObjCalc.regrad3(qtdIdoso, qtd) # quantidade de idosos
            time.sleep(1)
            print(f"\n\n1. Quantidade de participantes por gênero: \n\n| F | -> {femTQtdFim}%\n| M | -> {masTQtdFim}%\n")
            time.sleep(1)
            print(f"\n2. Faixa Etária dos participantes\n\n| J | -> {jovemQtdFim}% de jovens\n| A | -> {adultoQtdFim}% de adultos\n| I | -> {idosoQtdFim}% de idosos\n")
            time.sleep(1)
            print(f"\n3. Quantidade vacinados e de placebo\n\n| V | -> {vacinadosFim}% de vacinados\n| P | -> {placeboFim}% de placebo\n")
            time.sleep(1)
            print(f"\n4. Quantidade de infectados e não infectados\n\n| S | -> {contraiuSimFim}% de infectados\n| N | -> {contraiuNaoFim}% de não infectados\n\n")
            time.sleep(1)
            active = True
            return active

        if(self.escolha == '2'):
            # 100 * (a - b) / a
            a = 0
            b = 0
            for linha in arquivoLido:
                i = linha.split(',')
                # print(i)
                if(i[2] == 'V' and i[3] == 'S\n'):
                    b += 1
                elif(i[2] == 'P' and i[3] == 'S\n'):
                    a += 1

            if (a == 0):
                eficacia = 100 * (a - b)
            else:
                eficacia = 100 * (a - b)/a

            eficaciaFim = float("{:.2f}".format(eficacia))
            time.sleep(1)
            print(f'\n\nA eficácia geral da vacina é {eficaciaFim}%\n\n')
            time.sleep(1)
            active = True
            return active

        if(self.escolha == '3'):
            jovemPS = 0
            jovemVS = 0
            adultoPS = 0
            adultoVS = 0
            idosoPS = 0
            idosoVS = 0

            for linha in arquivoLido:
                i = linha.split(',')
                if((0 <= int(i[1]) <= 19) and (i[2] == 'P') and (i[3] == 'S\n')):
                    jovemPS += 1
                elif((0 <= int(i[1]) <= 19) and (i[2] == 'V') and (i[3] == 'S\n')):
                    jovemVS += 1
                elif((20 <= int(i[1]) <= 59) and (i[2] == 'P') and (i[3] == 'S\n')):
                    adultoPS += 1
                elif((20 <= int(i[1]) <= 59) and (i[2] == 'V') and (i[3] == 'S\n')):
                    adultoVS += 1
                elif(60 <= int(i[1]) and (i[2] == 'P') and (i[3] == 'S\n')):
                    idosoPS += 1
                elif(60 <= int(i[1]) and (i[2] == 'V') and (i[3] == 'S\n')):
                    idosoVS += 1

            jovemResultadoFim = 100 * (jovemPS - jovemVS)/jovemPS
            eficaciaFimJ = float("{:.2f}".format(jovemResultadoFim))
            adultoResultadoFim = 100 * (adultoPS - adultoVS)/adultoPS
            eficaciaFimA = float("{:.2f}".format(adultoResultadoFim))
            idosoResultadoFim = 100 * (idosoPS - idosoVS)/idosoPS
            eficaciaFimI = float("{:.2f}".format(idosoResultadoFim))

            time.sleep(1)
            print(f"\n\nEficácia da vacina por faixa etária\n\n| J | eficácia de {eficaciaFimJ}% entre os Jovens\n| A | eficácia de {eficaciaFimA}% entre os Adultos\n| I | eficácia de {eficaciaFimI}% entre Idosos\n\n")
            time.sleep(1)
            active = True
            return active

        if(self.escolha == '4'):
            eficaciaFemP = 0
            eficaciaFemV = 0
            eficaciaMasP = 0
            eficaciaMasV = 0
            for linha in arquivoLido:
                i = linha.split(',')
                if(i[0] == 'F' and i[2] == 'P' and i[3] == 'S\n'):
                    eficaciaFemP += 1
                elif(i[0] == 'F' and i[2] == 'V' and i[3] == 'S\n'):
                    eficaciaFemV += 1
                elif(i[0] == 'M' and i[2] == 'P' and i[3] == 'S\n'):
                    eficaciaMasP += 1
                elif(i[0] == 'M' and i[2] == 'V' and i[3] == 'S\n'):
                    eficaciaMasV += 1

            eficaciaFimF = 100 * (eficaciaFemP - eficaciaFemV)/eficaciaFemP
            eficaciaFimM = 100 * (eficaciaMasP - eficaciaMasV)/eficaciaMasP
            time.sleep(1)
            print(f"\n\nEficácia da vacina por Gênero\n\n| F | eficácia de {eficaciaFimF}% entre as Mulheres\n| M | eficácia de {eficaciaFimM}% entre os Homens")
            time.sleep(1)
            active = True
            return active


ObjExtractRotaDados = extractRotaDados()
