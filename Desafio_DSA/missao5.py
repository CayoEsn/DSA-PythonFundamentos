#!/usr/bin/env python
# coding: utf-8

# Versão da Linguagem Python
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from platform import python_version

print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# ## Missão: Analisar o Comportamento de Compra de Consumidores.

# ## Nível de Dificuldade: Alto

# Você recebeu a tarefa de analisar os dados de compras de um web site! Os dados estão no formato JSON e disponíveis junto com este notebook.
#
# No site, cada usuário efetua login usando sua conta pessoal e pode adquirir produtos à medida que navega pela lista de produtos oferecidos. Cada produto possui um valor de venda. Dados de idade e sexo de cada usuário foram coletados e estão fornecidos no arquivo JSON.
#
# Seu trabalho é entregar uma análise de comportamento de compra dos consumidores. Esse é um tipo de atividade comum realizado por Cientistas de Dados e o resultado deste trabalho pode ser usado, por exemplo, para alimentar um modelo de Machine Learning e fazer previsões sobre comportamentos futuros.
#
# Mas nesta missão você vai analisar o comportamento de compra dos consumidores usando o pacote Pandas da linguagem Python e seu relatório final deve incluir cada um dos seguintes itens:
#
# ** Contagem de Consumidores **
#
# * Número total de consumidores
#
#
# ** Análise Geral de Compras **
#
# * Número de itens exclusivos
# * Preço médio de compra
# * Número total de compras
# * Rendimento total
#
#
# ** Informações Demográficas Por Gênero **
#
# * Porcentagem e contagem de compradores masculinos
# * Porcentagem e contagem de compradores do sexo feminino
# * Porcentagem e contagem de outros / não divulgados
#
#
# ** Análise de Compras Por Gênero **
#
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Compras for faixa etária
#
#
# ** Identifique os 5 principais compradores pelo valor total de compra e, em seguida, liste (em uma tabela): **
#
# * Login
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Itens mais populares
#
#
# ** Identifique os 5 itens mais populares por contagem de compras e, em seguida, liste (em uma tabela): **
#
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# * Itens mais lucrativos
#
#
# ** Identifique os 5 itens mais lucrativos pelo valor total de compra e, em seguida, liste (em uma tabela): **
#
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
#
#
# ** Como considerações finais: **
#
# * Seu script deve funcionar para o conjunto de dados fornecido.
# * Você deve usar a Biblioteca Pandas e o Jupyter Notebook.
#

# Imports

# Carrega o arquivo
load_file = "dados_compras.json"
purchase_file = pd.read_json(load_file, orient="records")
purchase_file.head()

# # ## Informações Sobre os Consumidores

purchase_file = pd.read_json(load_file, orient="records")
# df.sort_values(by=['col1'])
purchase_file = purchase_file.drop_duplicates(subset='Login')
print('Número total de Consumidores: ' + str(len(purchase_file.index)))


# ## Análise Geral de Compras

purchase_file = pd.read_json(load_file, orient="records")
exclusive_products = purchase_file.drop_duplicates(subset='Item ID')
print('Número de itens exclusivos: ' + str(len(exclusive_products.index)))
print('Preço médio de compra: R$ %.2f' %
      (float(purchase_file.Valor.sum()) / float(len(purchase_file.index))))
print('Número total de compras: ' + str(len(purchase_file.index)))
print('Rendimento total: R$ %.2f' % (float(purchase_file.Valor.sum())))


# # ## Análise Demográfica

purchase_file = pd.read_json(load_file, orient="records")
countTotal = len(purchase_file.index)
countMasculino = len(purchase_file[purchase_file['Sexo'] == 'Masculino'])
countFeminino = len(purchase_file[purchase_file['Sexo'] == 'Feminino'])
countOutros = len(purchase_file[(purchase_file['Sexo'] != 'Masculino') & (
    purchase_file['Sexo'] != 'Feminino')])
# print('Porcentagem e contagem de compradores masculinos: %.2f %% | %d' % ((countMasculino / countTotal) * 100, countMasculino))
# print('Porcentagem e contagem de compradores do sexo feminino: %.2f %% | %d' % ((countFeminino / countTotal) * 100, countFeminino))
# print('Porcentagem e contagem de outros / não divulgados: %.2f %% | %d' % ((countOutros / countTotal) * 100, countOutros))

labelsCount = [countMasculino, countFeminino, countOutros]
labels = [str(countMasculino) + ' ['+str(round((countMasculino / countTotal) * 100, 2)) + '%' + ']',
          str(countFeminino) +
          ' ['+str(round((countFeminino / countTotal) * 100, 2)) + '%' + ']',
          str(countOutros) + ' ['+str(round((countOutros / countTotal) * 100, 2)) + '%' + ']']
cs = cm.Set3(np.arange(100))

# Cria a figura
f = plt.figure()

# Pie Plot
plt.pie(labelsCount, labeldistance=1, radius=3,
        colors=cs, wedgeprops=dict(width=0.8))
plt.legend(labels=labels, loc='center', prop={'size': 12})
plt.title("Porcentagem e contagem de compradores", loc='Center',
          fontdict={'fontsize': 20, 'fontweight': 20})
plt.show()

# # ## Análise de Compras Por Gênero

others = {}
purchase_file = pd.read_json(load_file, orient="records")

data = purchase_file.groupby('Sexo').describe()
others['Sexo'] = purchase_file['Sexo'].drop_duplicates().tolist()
others['Número de compras'] = [int(valor)
                               for valor in data['Valor']['count'].tolist()]
others['Preço médio de compra'] = [
    round(mean, 2) for mean in data['Valor']['mean'].tolist()]
others['Valor Total de Compra'] = purchase_file[[
    'Valor', 'Sexo']].groupby('Sexo').sum()['Valor'].tolist()

comprasFaixaEtaria = purchase_file[['Sexo', 'Idade', 'Valor']].groupby(
    ['Sexo', 'Idade'], as_index=False).mean()
comprasFaixaEtaria = [[item[0], item[1], round(
    item[2], 2)] for item in comprasFaixaEtaria.itertuples(index=False, name=None)]

df = pd.DataFrame(others, columns=('Sexo', 'Número de compras',
                                   'Preço médio de compra', 'Valor Total de Compra'))
blankIndex = [''] * len(df)
df.index = blankIndex
print(df)

pd.set_option("max_rows", None, "max_columns", None)
df2 = pd.DataFrame(comprasFaixaEtaria, columns=(
    'Sexo', 'Idade', 'Preço médio de compra'))
blankIndex2 = [''] * len(df2)
df2.index = blankIndex2
print(df2)

# # ## Consumidores Mais Populares (Top 5)

purchase_file = pd.read_json(load_file, orient="records")
consumidoresMaisPopularesOriginal = purchase_file[[
    'Login', 'Valor', 'Item ID']].groupby(['Login', 'Valor'], as_index=False).mean()
consumidoresMaisPopulares = consumidoresMaisPopularesOriginal.groupby(
    ['Login'], as_index=False).sum()
consumidoresMaisPopulares['Item ID'] = consumidoresMaisPopularesOriginal.groupby(
    ['Login'], as_index=False).count()['Item ID']
consumidoresMaisPopulares = consumidoresMaisPopulares.sort_values(
    by='Valor', ascending=False).head()
data = [[item[0], round(item[1], 2), item[2]]
        for item in consumidoresMaisPopulares.values]

df = pd.DataFrame(data, columns=(
    'Login', 'Valor Total de Compra', 'Número de compras'))
blankIndex = [''] * len(df)
df.index = blankIndex
print(df)

resultadoMaisPopulares = purchase_file[purchase_file['Login'].isin(
    consumidoresMaisPopulares['Login'].tolist())]
valorTotalCompras = resultadoMaisPopulares['Valor'].sum()
precoMedioCompras = round(resultadoMaisPopulares['Valor'].mean(), 2)
produtosMaisVendidos = purchase_file[['Nome do Item', 'Item ID']].groupby(
    ['Nome do Item']).size().reset_index(name='count').sort_values(by='count', ascending=False).head()
data2 = [[item[0], round(item[1], 2)] for item in produtosMaisVendidos.values]

df2 = pd.DataFrame(data2, columns=('Nome do Item', 'Quantidade Vendida'))
blankIndex2 = [''] * len(df2)
df2.index = blankIndex2
print(df2)

# # ## Itens Mais Populares

itens = {}
purchase_file = pd.read_json(load_file, orient="records")

data = purchase_file[['Nome do Item', 'Item ID', 'Valor']].groupby(
    ['Item ID', 'Nome do Item', 'Valor']).size().reset_index(name='count')
data['total'] = data['Valor'] * data['count']
data = data.sort_values(by='count', ascending=False).head()
dataFinal = [[item[0], item[1], round(item[2], 2), item[3], round(
    item[4], 2)] for item in data.itertuples(index=False, name=None)]

df = pd.DataFrame(dataFinal, columns=('ID do item ', 'Nome do item',
                                      'Preço do item', 'Número de compras', 'Valor Total de Compra'))
blankIndex = [''] * len(df)
df.index = blankIndex
print(df)

# # ## Itens Mais Lucrativos

itens = {}
purchase_file = pd.read_json(load_file, orient="records")

data = purchase_file[['Nome do Item', 'Item ID', 'Valor']].groupby(
    ['Item ID', 'Nome do Item', 'Valor']).size().reset_index(name='count')
data['total'] = data['Valor'] * data['count']
data = data.sort_values(by='total', ascending=False).head()
dataFinal = [[item[0], item[1], round(item[2], 2), item[3], round(
    item[4], 2)] for item in data.itertuples(index=False, name=None)]

df = pd.DataFrame(dataFinal, columns=('ID do item ', 'Nome do item',
                                      'Preço do item', 'Número de compras', 'Valor Total de Compra'))
blankIndex = [''] * len(df)
df.index = blankIndex
print(df)
