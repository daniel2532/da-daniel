import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
preco = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
 grafico = sns.lineplot(data=preco, x="dia", y="venda", palette="pastel")

 grafico.set(title='Preço da gasolina por dia', xlabel='Dia', \
 ylabel='Preço');
 plt.savefig('grafico.png')
