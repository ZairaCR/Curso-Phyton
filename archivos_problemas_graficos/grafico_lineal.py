import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\flores.csv")
print(df)

#creando el grafico
sns.lineplot(x="fecha", y="flores",data=df)

#creando un punto en el dia de mas flores
plt.plot("01-09",17,"o")

#mostrando el grafico
plt.show()