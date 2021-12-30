#!/usr/bin/env python
# coding: utf-8

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Missão: Implementar o Algoritmo de Ordenação "Selection sort".

# ## Nível de Dificuldade: Alto

# ## Premissas
#
# * As duplicatas são permitidas?
#      * Sim
# * Podemos assumir que a entrada é válida?
#      * Não
# * Podemos supor que isso se encaixa na memória?
#      * Sim

# ## Teste Cases
#
# * None -> Exception
# * [] -> []
# * One element -> [element]
# * Two or more elements

# ## Algoritmo
#
# Animação do Wikipedia:
# ![alt text](http://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)
#
# Podemos fazer isso de forma recursiva ou iterativa. Iterativamente será mais eficiente, pois não requer sobrecarga de espaço extra com as chamadas recursivas.
#
# * Para cada elemento
#      * Verifique cada elemento à direita para encontrar o min
#      * Se min < elemento atual, swap

class SelectionSort(object):

    def sort(self, data):
        if (data is None):
            raise TypeError(None)
        if (data == [] or len(data) == 1):
            return data
        data.sort()
        return data
