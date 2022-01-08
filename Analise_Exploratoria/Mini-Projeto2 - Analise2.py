#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
#
# ## Download: http://github.com/dsacademybr
#
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
#
# ## Análise 2

# Imports
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")
# get_ipython().run_line_magic('matplotlib', 'inline')

# Dataset
clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path, encoding="latin-1")


# ## Número de veículos pertencentes a cada marca

sns.set(rc={'figure.figsize': (10, 12)})
countplot = sns.countplot(y="brand", data=df)
countplot.set(xlabel='Número de Veículos', ylabel='Marca')
[countplot.annotate(count.get_height(), (count.get_x()+0.1,
                                         count.get_height()+1500)) for count in countplot.patches]
countplot.show()

# Salvando o plot
fig = countplot.get_figure()
fig.savefig(("plots/Analise2/brand-vehicleCount.png"))


# ## Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio

# Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio

priceGearManuell = df[df['gearbox'] == 'manuell'][[
    'price', 'vehicleType']].groupby(['vehicleType']).mean().reset_index()
priceGearAutomatik = df[df['gearbox'] == 'automatik'][[
    'price', 'vehicleType']].groupby(['vehicleType']).mean().reset_index()
priceGearUnspecified = df[df['gearbox'] == 'Unspecified'][[
    'price', 'vehicleType']].groupby(['vehicleType']).mean().reset_index()

dtPlot = pd.DataFrame({'manuell': priceGearManuell['price'].array,
                       'automatik': priceGearAutomatik['price'].array,
                       'Unspecified': priceGearUnspecified['price'].array}, index=priceGearManuell['vehicleType'])
plotbar = dtPlot.plot.bar(rot=0)
plotbar.show()

# Salvando o plot
fig = plotbar.get_figure()
fig.savefig("plots/Analise2/vehicletype-gearbox-price.png")
