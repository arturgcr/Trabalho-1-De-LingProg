## Lógica do código:
## 1 - pedir pra usuario selecionar as tags de interesse 
## 2 - seleciar nome das pessoas com tag em comum
## 3 - criar um dicionario com o nome de cada membro que inclua as strings (nome e horario) com os valores (1 - marcado) / (0 - nao marcado)
## 4 - criar um dicionario e associar as strings (nome e horario) com a quantidade de pessoas que marcaram essse horario


# Bloco de código responsável por criar o dicionaria de todos os harários
dicionarioDeHorarios = {}
listaDeCheckBoxes = []

for checkboxe in listaDeCheckBoxes:
    dicionarioDeHorarios.update({str(listaDeCheckBoxes[checkboxe]), 0})


