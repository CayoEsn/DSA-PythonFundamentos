#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
#
# ## Download: http://github.com/dsacademybr
#
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
#
# ## Análise 3

# In[2]:


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


# ## Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio

priceGear = df[['price', 'fuelType', 'gearbox']].groupby(
    ['fuelType', 'gearbox']).mean().reset_index()
barplot = sns.barplot(x="fuelType", y="price", hue="gearbox", data=priceGear)
barplot.set(xlabel='Tipo de Combustível', ylabel='Preço Médio')
barplot.show()

# Salvando o plot
fig = barplot.get_figure()
fig.savefig("plots/Analise3/fueltype-vehicleType-price.png")


# ## Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio

# Crie um Barplot com a Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio
pricePowerPS = df[['powerPS', 'vehicleType', 'gearbox']].groupby(
    ['vehicleType', 'gearbox']).mean().reset_index()
barplot2 = sns.barplot(x="vehicleType", y="powerPS",
                       hue="gearbox", data=pricePowerPS)
barplot2.set(title='Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio',
             xlabel='Tipo de Combustível', ylabel='Potência Média')
barplot2.show()

# Salvando o plot
fig = barplot2.get_figure()
fig.savefig("plots/Analise3/vehicletype-fueltype-power.png")
