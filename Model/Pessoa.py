class Pessoa:

    def __init__(self):
        self.__sexo = ""
        self.__peso = 0.0
        self.__altura = 0.0

    def setSexo(self, sexo):
        self.__sexo = sexo

    def getSexo(self):
        return self.__sexo

    def setPeso(self, peso):
        self.__peso = peso

    def getPeso(self):
        return self.__peso

    def setAltura(self, altura):
        self.__altura = altura

    def getAltura(self):
        return self.__altura

    def calcularImc(self):
        imc = self.__peso / (self.__altura ** 2)
        return imc

    def resultadoImc(self):
        if self.__sexo == "Feminino" or self.__sexo == "Masculino":
            if self.__sexo == "Feminino":
                if self.calcularImc() < 19.1:
                    return f"\nIMC = {self.calcularImc():.2f}, abaixo do peso, IMC do peso normal entre 19.1 e 25.7."
                else:
                    if 19.1 <= self.calcularImc() < 25.8:
                        return f"\nIMC = {self.calcularImc():.2f}, no peso normal."
                    else:
                        if 25.8 <= self.calcularImc() < 27.3:
                            return f"\nIMC = {self.calcularImc():.2f}, marginalmente acima do peso, IMC do peso normal entre 19.1 e 25.7."
                        else:
                            if 27.3 <= self.calcularImc() < 32.3:
                                return f"\nIMC = {self.calcularImc():.2f}, acima do peso ideal, IMC do peso normal entre 19.1 e 25.7."
                            else:
                                return f"\nIMC = {self.calcularImc():.2f}, obesa, IMC do peso normal entre 19.1 e 25.7."
            else:
                if self.__sexo == "Masculino":
                    if self.calcularImc() < 20.7:
                        return f"\nIMC = {self.calcularImc():.2f}, abaixo do peso, IMC do peso normal entre 19.1 e 25.7."
                    else:
                        if 20.7 <= self.calcularImc() < 26.4:
                            return f"\nIMC = {self.calcularImc():.2f}, no peso normal."
                        else:
                            if 26.4 <= self.calcularImc() < 27.8:
                                return f"\nIMC = {self.calcularImc():.2f}, marginalmente acima do peso, IMC do peso normal entre 19.1 e 25.7."
                            else:
                                if 27.8 <= self.calcularImc() < 31.1:
                                    return f"\nIMC = {self.calcularImc():.2f}, acima do peso ideal, IMC do peso normal entre 19.1 e 25.7."
                                else:
                                    return f"\nIMC = {self.calcularImc():.2f}, obeso, IMC do peso normal entre 19.1 e 25.7."
        else:
            return f"\nSexo: {self.__sexo} está errado, digite Masculino ou Feminino no atributo sexo."
