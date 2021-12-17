# Calculadora em Python

def soma(num1, num2):
    print('%d + %d = %d' % (num1, num2, num1 + num2))

def subtracao(num1, num2):
    print('%d - %d = %d' % (num1, num2, num1 - num2))

def multiplicacao(num1, num2):
    print('%d x %d = %d' % (num1, num2, num1 * num2))

def divisao(num1, num2):
    print('%d / %d = %d' % (num1, num2, num1 / num2))

opcao = int(input('Digite sua opção (1/2/3/4): '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if (opcao == 1): soma(num1, num2)
elif (opcao == 2): subtracao(num1, num2)
elif (opcao == 3): multiplicacao(num1, num2)
elif (opcao == 4): divisao(num1, num2)
else: print('Opção Inválida!')