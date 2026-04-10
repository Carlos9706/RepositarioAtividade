print("Calculadora")
print("Digite um número válido dentre as opções de menu: ")

while True:
    print("--- Menu da Calculadora ---")
    print("1 - Soma")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")
    print("5 - sair")

    try:
        opcoes = int(input("Digite uma opção do menu: "))
    except ValueError:
        print("Erro, opção invalida!!")
        continue

    if opcoes == 5:
        print("Saindo da calculadora.....")
        break

    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Erro!!, digite números válidos!")
        continue

    if opcoes == 1:
        resultado = numero1 + numero2
        print("A soma é: {}".format(resultado))

    elif opcoes == 2:
        resultado = numero1 - numero2
        print("A subtração é: {}".format(resultado))

    elif opcoes == 3:
        resultado = numero1 * numero2
        print("A multiplicação é: {}".format(resultado))

    elif opcoes == 4:
        if numero2 == 0:
            print("Erro, não é possivel dividir por Zero!!")
        else:
            resultado = numero1 / numero2
            print("A divisão é: {}".format(resultado))

    else:
        print("Opção invalida!")