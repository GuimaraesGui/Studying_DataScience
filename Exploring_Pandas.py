import pandas as pd

lista = [12, 23, 34, 45, 56, 67]

serie_pandas = pd.Series(lista)

print(serie_pandas[2])

notas = {'Guilherme':7.2, 'Vicktoria': 9.5, 'Heloisa': 5.4}
serie_notas = pd.Series(notas)

print(serie_notas)
print(serie_notas.mean()) #Usando NumPy + Pandas

print(serie_notas.median()) #Mediana, funçãoe exclusiva do Pandas

print(serie_notas.describe()) #Exibe dados gerais, função exclusiva do Pandas