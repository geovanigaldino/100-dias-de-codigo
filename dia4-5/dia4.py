def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def calculadora():

    while True:
        print("\n CALCULADORA")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão \n")

        escolha = input("Selecione uma operação (1/2/3/4): \n")

        if escolha in ('1','2','3','4'):
            primeiroNumero = int(input("Digite o primeiro número: "))
            segundoNumero = int(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {adicao(primeiroNumero, segundoNumero)}.")
            if escolha == '2':
                print(f"Resultado: {subtracao(primeiroNumero, segundoNumero)}.")
            if escolha == '3':
                print(f"Resultado: {multiplicacao(primeiroNumero, segundoNumero)}.")
            if escolha == '4':
                if segundoNumero != 0:
                    print(f"Resultado: {divisao(primeiroNumero, segundoNumero)}.")
                else:
                    print("Não é permitida a divisão por zero.")
        else:
            print("Escolha inválida.")

        continuar = input("Deseja fazer outra operação? (s/n)")
        if continuar == "n":
            print("Calculadora encerrada.")
            break;

calculadora()