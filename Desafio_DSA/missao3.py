#!/usr/bin/env python
# coding: utf-8

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Missão: Implementar um algoritmo para mover um robô do canto superior esquerdo para o canto inferior direito de uma grade.

# ## Nível de Dificuldade: Médio

# ## Premissas
#
# * Existem restrições de como o robô se move?
#      * O robô só pode se mover para a direita e para baixo
# * Algumas células são inválidas (fora dos limites)?
#      * Sim
# * Podemos supor que as células inicial e final são células válidas?
#      * Sim
# * Isso é uma grade retangular? ou seja, a grade não é irregular?
#      * Sim
# * Haverá sempre uma maneira válida para o robô chegar ao canto inferior direito?
#      * Não, retorno None
# * Podemos assumir que as entradas são válidas?
#      * Não
# * Podemos supor que isso se encaixa na memória?
#      * Sim

# ## Teste Cases
#
# <pre>
# o = célula válida
# x = célula inválida
#
#    0  1  2  3
# 0  o  o  o  o
# 1  o  x  o  o
# 2  o  o  x  o
# 3  x  o  o  o
# 4  o  o  x  o
# 5  o  o  o  x
# 6  o  x  o  x
# 7  o  x  o  o
# </pre>
#
# * Caso geral
#
# ```
# Saída esperada = [(0, 0), (1, 0), (2, 0),
#                   (2, 1), (3, 1), (4, 1),
#                   (5, 1), (5, 2), (6, 2),
#                   (7, 2), (7, 3)]
# ```
#
# * Nenhum caminho válido, por exemplo, linha 7, col 2 é inválido
# * Nenhuma entrada
# * Matriz vazia

class Grid(object):

    def find_path(self, matrix):
        if (matrix is None or matrix == [[]]):
            return None

        x_atual = y_atual = 0
        caminho = [(x_atual, y_atual)]
        processando = True

        while(processando):
            if (x_atual < 7 and matrix[x_atual + 1][y_atual] == 1):
                x_atual = x_atual + 1
                caminho.append((x_atual, y_atual))
            elif (y_atual < 3 and matrix[x_atual][y_atual + 1] == 1):
                y_atual = y_atual + 1
                caminho.append((x_atual, y_atual))
            else:
                caminho = None
                processando = False

            if (x_atual == 7 and y_atual == 3):
                processando = False

        return caminho
