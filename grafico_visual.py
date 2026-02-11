import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('relatorio_churn.xlsx')

contagem = df['status'].value_counts()
contagem.plot(kind='bar')

plt.title('Gráfico de Retenção')
plt.xticks(rotation=0)
plt.xlabel('Status')
plt.ylabel('Quantidade')
plt.show()