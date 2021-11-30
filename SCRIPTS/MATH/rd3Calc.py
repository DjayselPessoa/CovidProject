class calc:

    def regrad3(self, recebe, qtdTotal, ):
        self.recebe = recebe
        self.qtdTotal = qtdTotal

        x = (self.recebe * 100)/self.qtdTotal

        return x


ObjCalc = calc()
