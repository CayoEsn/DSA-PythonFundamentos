#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
#
# ## Download: http://github.com/dsacademybr
#
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
#
# ## Análise 4

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

# Calcule a média de preço por marca e por veículo
df[['price', 'brand', 'vehicleType']].groupby(
    ['vehicleType', 'brand']).mean().reset_index().head()


# ## Preço médio de um veículo por marca, bem como tipo de veículo

dfHeat = df[['price', 'brand', 'vehicleType']].groupby(
    ['vehicleType', 'brand']).mean().reset_index()
heatmap = dfHeat.pivot("brand", "vehicleType")
heatmap = sns.heatmap(heatmap, cmap="YlGnBu", annot=True)
heatmap.set(title='HeatMap - Preço Médio de um Veículo por Marca e Tipo de Veículo',
            xlabel='Tipo de Veículo', ylabel='Marca')
heatmap.show()

# Salvando o plot
fig = heatmap.get_figure()
fig.savefig("plots/Analise4/heatmap-price-brand-vehicleType.png")
