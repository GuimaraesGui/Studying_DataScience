import numpy as np

def imprimirLinha():
    print("\n______________")

lista = [1, 2, 3, 4, 5]
array = np.array(lista) # np.array() converte em ndarray. Os parâmetros são os valores do array antigo.

print(type(lista))
print(type(array))

array_zeros = np.zeros(10) # np.zeros(): Cria um array de zeros. O parâmetro é a quantidade de zeros dentro do array.

print("\n", array_zeros)

## Matrizes
matriz_zeros = np.zeros([3,3])

print("\n", matriz_zeros)

##Equações matemáticas
lista_de_notas = [9.8, 5.6, 7.8, 9.1, 6.5]

notas = np.array(lista_de_notas)

print("\n")
print('Máximo: ', np.max(notas))
print("\n")
print('Mínimo: ', np.min(notas))
print("\n")
print('Média: ', np.mean(notas))
print("\n")
print('Desvio padrão: ', np.std(notas))
print("\n")
print('Posição da menor nota: ', np.argmin(notas))
print("\n")
print('Posição da maior nota: ', np.argmax(notas))
print("\n")

## Máscara de dados
is_covid_positive = np.array(['Yes', 'No', 'No', 'Yes', 'Yes', 'No'])
mask = (is_covid_positive == 'Yes')

print(is_covid_positive)
print(mask)

print("\n")

is_covid_positive[mask] = 'C19'
print(is_covid_positive)

imprimirLinha()

notas = np.array([4.9, 6.5, 3.2, 6.7])
aprovado = (notas >=6)
reprovado = (notas <6)
notas[aprovado] = True
notas[reprovado] = False
print(notas)