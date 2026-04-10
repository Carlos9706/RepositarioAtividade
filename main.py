print("Calculadora")
print("Digite um número válido dentre as opções de menu: ")

print("--- Menu da Calculadora ---")
print("1 - Soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")

opcoes = int(input("Digite uma opção do menu: "))


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("A soma é: {}".format(soma))
print("A subtração é: {}".format(subtracao))
print("A multiplicação é: {}".format(multiplicacao))
print("A divisão é: {}".format(divisao))