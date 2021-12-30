#!/usr/bin/env python
# coding: utf-8

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Missão: Implementar um algoritmo para determinar se uma string possui todos os caracteres exclusivos.

# ## Nível de Dificuldade: Baixo

# ## Premissas
#
# * Podemos assumir que a string é ASCII?
#      * Sim
#      * Nota: As cadeias de caracteres Unicode podem exigir tratamento especial dependendo do seu idioma
# * Podemos supor que há distinção entre maiúsculas e minúsculas?
#      * Sim
# * Podemos usar estruturas de dados adicionais?
#      * Sim

# ## Teste Cases
#
# * None -> False
# * '' -> True
# * 'foo' -> False
# * 'bar' -> True

# ## Algoritmo: Hash Map Lookup
#
# Manteremos um mapa hash (conjunto) para rastrear os caracteres únicos que encontramos.
#
# Passos:
# * Faça um scan cada caracter
# * Para cada caracter:
#      * Se o caracter não existir em um mapa de hash, adicione o caractere a um mapa de hash
#      * Senão, retorne False
# * Retornar Verdadeiro
#
# Nota:
# * Também podemos usar um dicionário, mas parece mais lógico usar um set, pois ele não contém elementos duplicados

# ## Solução

class UniqueChars(object):

    def has_unique_chars(self, string):
        if (string is None):
            return False
        if (len(string) == 0):
            return True
        retorno = True
        for word in string:
            if string.count(word) > 1:
                retorno = False
        return retorno
