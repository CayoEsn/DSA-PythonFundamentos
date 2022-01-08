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

# Dataset
clean_data_path = "Analise_Exploratoria/dataset/autos.csv"
df = pd.read_csv(clean_data_path, encoding="latin-1")


# ## Distribuição de Veículos com base no Ano de Registro

# Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
sns.set(rc={'figure.figsize': (10, 8)})
distplot = sns.distplot(df['yearOfRegistration'])
plt.show()

# Salvando o plot
fig = distplot.get_figure()
fig.savefig("Analise_Exploratoria/plots/Analise1/vehicle-distribution.png")


# ## Variação da faixa de preço pelo tipo de veículo

boxplot = sns.boxplot(x="vehicleType", y="price", data=df)
boxplot.set(xlabel='Tipo de Veículo', ylabel='Range de Preço')
sns.despine(offset=10, trim=True)
plt.show()

# Salvando o plot
fig = boxplot.get_figure()
fig.savefig("Analise_Exploratoria/plots/Analise1/price-vehicleType-boxplot.png")


# ## Contagem total de veículos à venda conforme o tipo de veículo

countplot = sns.countplot(x="vehicleType", data=df)
countplot.set(xlabel='Tipo de Veículo', ylabel='Total de Veiculos Para Venda')
[countplot.annotate(count.get_height(), (count.get_x()+0.1,
                                         count.get_height()+1500)) for count in countplot.patches]
countplot
plt.show()

# Salvando o plot
fig = countplot.get_figure()
fig.savefig("Analise_Exploratoria/plots/Analise1/count-vehicleType.png")
