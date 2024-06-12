import pandas as pd

dictionary = {'Autores': ['Rick Riordan', 'J. R. R. Tolkien', 'Rick Riordan', 'Machado de Assis'],
        'Títulos': ['O Ladrão de Raios', "A Sociedade do Anel", "Mar de Monstros", 'Memórias Postumas de Brás Cubas'],
        'Preços': [41.2, 35.7, 39.5, 40.5]}

df = pd.DataFrame(dictionary) # Sintaxe para criar um DataFrame: <nomeDoDataFrame> = pd.DataFrame(<parâmetros>).
print(df)                     # O parâmetro corresponde ao array de referência.

#Filtrando por Autor
print("\n")
print(df['Autores'])    # Para fazer referência ao DataFrame, usas-se:<nomeDoDataFrame>[<nomeDaColuna>]

#Filtrando pelo nº do autor
print("\n")
print(df['Autores'][1]) # Para visualizar somente uma linha, especificar através de:
                        # <nomeDoDataFrame>[<nomeDaColuna>][<numero da linha>]

#Aplicando calculos as colunas
print("\n")
                            # Para aplicar funções basta:
print(df['Preços'].mean())  # <nomeDoDataFrame>[<nomeDaColuna>].function()
                            
#Filtrando todos os livros de um autor, no caso, Rick Riordan
"""
Aplicando o conceito de máscaram criamos a variável 'mask', que recebe o teste lógico da coluna da coluna do DataFrame em relação ao valor desejado.
Funciona um filtro, onde verificamos se a coluna do DataFrame possui ou não o autor. Caso não encontre, retornará um df vazio.   
"""
autor = input('\nQual é o autor desejado? ')
mask = (df['Autores'] == autor) 

print('\nSelecionando um autor:\n ', df[mask]) ## Então, associar o DataFrame com a 'mask' <nomeDoDataFrame>[mask]

#Inserindo/Concatenando DataFrames
"""
1º) Criar um novo df com os dados a serem inseridos.
2º) Concatenar com o df antigo:
        <nomeDoNovoDataFrame> = pd.DataFrame(<parâmetros>)
        <nomeDoAntigoDataFrame> = pd.concat([<nomeDoAntigoDataframe>, <nomeDoNovoDataFrame>])
"""
nova_linha = pd.DataFrame({'Autores': ['Rick Riordan'],
                           'Títulos': ['A Maldiçã do Titã'],
                           'Preços': [50.1]})
df = pd.concat([df, nova_linha], ignore_index=True) #ignore_index serve para manter a indexação.

print("\nDataFrame após a inserção da nova linha: ")
print(df)

# Substituindo o valor de uma linha
"""
Para subsituir, usa-se a função '.loc': <nomeDoDataFrame>.loc[<linha>,<coluna>]
Além disso, podemos criar uma 'máscara de correção', que faz referência com o item e o substitui.
"""
mask_correcão = (df['Títulos'] == 'A Maldiçã do Titã')
df.loc[mask_correcão, 'Títulos'] = 'A Maldição do Titã'
print('\nCorrigido: \n', df)