# Anotações sobre a biblioteca Openpyxl

1. Carregando uma planilha (workbook):
```python
workbook = openpyxl.load_workbook('endereçoArquivo')
```

1. Acessando uma aba (worksheet):

Acessando uma worksheet ativa:

```Python
ws = workbook.active
```

Acessando uma planilha específica:
```Python
ws = workbook['nomeAba']
```

3. Acessando uma célula
```Python
ws['colunaELinha']
# Forma alternativa
celula = planilha.cell(row=1, column=1)
```

4. Inserindo valor na célula
```Python
ws['A1'].value = 'Novo valor'
```

5. Exibindo o valor da célula
```Python
ws['colunaELinha'].value
```

6. Salvando alterações
```Python
workbook.save('endereçoArquivo')
```

7. Criando uma planilha
```Python
from openpyxl import Workbook
# Criando a planilha
workbook = Workbook()

# Salvando a planilha
workbook.save('nomeArquivo.xlsx')
```