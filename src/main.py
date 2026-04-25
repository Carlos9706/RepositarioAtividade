def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        raise ValueError("Não é possivel dividir por Zero!")
    return num1 / num2


def executar_calculadora():
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
            print("A soma é: " + soma(numero1, numero2))

        elif opcoes == 2:
            print("A subtração é: " + subtracao(numero1, numero2))

        elif opcoes == 3:
            print("A multiplicação é: " + multiplicacao(numero1, numero2))

        elif opcoes == 4:
            try:
                 print("A divisão é: " + divisao(numero1, numero2))
            except ValueError as e:
                print(e)
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    executar_calculadora()

