from Model.Pessoa import Pessoa

if __name__ == "__main__":

    # Digitar Masculino ou Feminino para sexo
    # Criando pessoa

    pessoa1 = Pessoa()
    pessoa1.setSexo("Feminino")
    pessoa1.setPeso(70)
    pessoa1.setAltura(1.50)

    pessoa2 = Pessoa()
    pessoa2.setSexo("Masculino")
    pessoa2.setPeso(72)
    pessoa2.setAltura(1.70)

    pessoa3 = Pessoa()
    pessoa3.setSexo("Masculino")
    pessoa3.setPeso(58)
    pessoa3.setAltura(1.68)

    # Criando pessoa com erro no sexo para testar verificador

    pessoa4 = Pessoa()
    pessoa4.setSexo("Femini")
    pessoa4.setPeso(85)
    pessoa4.setAltura(1.78)

    # Calculando IMC e conferindo tabela

    calculo1 = pessoa1.resultadoImc()
    calculo2 = pessoa2.resultadoImc()
    calculo3 = pessoa3.resultadoImc()
    calculo4 = pessoa4.resultadoImc()

    # Printando resultado de cada pessoa

    print("Calculo de IMC")

    print(calculo1)
    print(calculo2)
    print(calculo3)
    print(calculo4)

    print("\nPrograma finalizado.")
