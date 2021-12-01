# from pathlib import Path
# import os
from DATA.eRD import ObjExtractRotaDados # eRD - extract rota dados


class controlCore:
    try:

        def control(self, escolha, pegarDirRaiz):
            self.escolha = escolha
            self.pegarDirRaiz = pegarDirRaiz

            if(self.escolha == '0'):
                active = ObjExtractRotaDados.extract(self.escolha, self.pegarDirRaiz)
                return active
            if(self.escolha == '1'):
                active = ObjExtractRotaDados.extract(self.escolha, self.pegarDirRaiz)
                return active
            if(self.escolha == '2'):
                active = ObjExtractRotaDados.extract(self.escolha, self.pegarDirRaiz)
                return active
            if(self.escolha == '3'):
                active = ObjExtractRotaDados.extract(self.escolha, self.pegarDirRaiz)
                return active
            if(self.escolha == '4'):
                active = ObjExtractRotaDados.extract(self.escolha, self.pegarDirRaiz)
                return active
    except:
        print("- ERRO DESCONHECIDO -")


ObjControlCore = controlCore()
