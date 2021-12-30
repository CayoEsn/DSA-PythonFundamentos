#!/usr/bin/env python
# coding: utf-8

# Versão da Linguagem Python
import math
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Missão: Gerar uma lista de números primos.

# ## Nível de Dificuldade: Médio

# ## Premissas
#
# * É correto que 1 não seja considerado um número primo?
#      * Sim
# * Podemos assumir que as entradas são válidas?
#      * Não
# * Podemos supor que isso se encaixa na memória?
#      * Sim

# ## Teste Cases
#
# * None -> Exception
# * Not an int -> Exception
# * 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

# ## Algoritmo
#
# Para um número ser primo, ele deve ser 2 ou maior e não pode ser divisível por outro número diferente de si mesmo (e 1).
#
# Todos os números não-primos são divisíveis por um número primo.
#
# * Use uma matriz (array) para manter o controle de cada número inteiro até o máximo
# * Comece em 2, termine em sqrt (max)
#      * Podemos usar o sqrt (max) em vez do max porque:
#          * Para cada valor que divide o número de entrada uniformemente, há um complemento b onde a * b = n
#          * Se a> sqrt (n) então b <sqrt (n) porque sqrt (n ^ 2) = n
#      * "Cross off" todos os números divisíveis por 2, 3, 5, 7, ... configurando array [index] para False
#
# Animação do Wikipedia:
#
# ![alt text](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

# ## Solução


class PrimeGenerator(object):

    def generate_primes(self, max_num):
        if (max_num is None):
            raise TypeError(None)
        if (isinstance(max_num, float)):
            raise TypeError(None)
        multiplos = 0
        primos = []
        for num1 in range(max_num):
            if num1 == 0 or num1 == 1:
                primos.append(False)
                continue

            for num2 in range(1, num1):
                if (num1 % num2 == 0):
                    multiplos += 1
            if (multiplos == 1):
                primos.append(True)
            else:
                primos.append(False)
            multiplos = 0
        return primos
