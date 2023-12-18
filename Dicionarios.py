""" DICIONARIOS """

# Variável composta.
# Representado por {}.
# Por exemplo : 

# Dicionario = {}
# Ou assim 
# Dicionario = dict()
# Recebe indices literais.
#Divido em chaves e valores = Keys e Values.

# Exemplos : 

dados = dict()
dados = {'Nome' : 'Pedro', 'Idade' : '25' }
print(dados)
print(dados['Nome']) # Vai me mostrar o nome
print(dados['Idade']) # Vai me mostrar a idade 

# Adicionando valores num dicionário.
#Por exemplo:
dados = dict()
dados = {'Nome' : 'Pedro', 'Idade' : '25' }
dados['Sexo'] = 'M' # Vai adicionar a chave sexo com o valor m no final do dicionário.
print(dados)

# Deletando valores num dicionário.
dados = dict()
dados = {'Nome' : 'Pedro', 'Idade' : '25' , 'Sexo' : 'M'}
del dados['Idade'] # Vou deletar a chave e o valor da idade.
print(dados)

# Outro exemplo :

filmes = dict()
filmes = {'Título' : 'Star Wars', 'Ano' : '1977', 'Diretor' : 'George Lucas'}
print(filmes.values()) # Vai me retornar os valores contidos nas minhas chaves, Star wars, 1977 e George Lucas
print(filmes.keys()) # Vai me retornar as chaves que são Título, Ano e Diretor.
print(filmes.items()) # Vai me retornar as chaves e meus valores.

# Usando loops em dicionários.
filmes = dict()
filmes = {'Título' : 'Star Wars', 'Ano' : '1977', 'Diretor' : 'George Lucas'}
for k,v in filmes.items(): # Aqui vou mostrar minha chave e seu correspondente valor. 
    print(f'O {k} é {v}')

# Juntando listas com dicionários.
locadora = []
locadora = [{'Título': 'Star Wars', 'Ano' : '1977', 'Diretor' : 'George Lucas'}
            , {'Título' : 'Avengers', 'Ano' : '2015', 'Diretor' : 'Joss Whedon'},
            {'Título' : 'Matrix', 'Ano' : '1999', 'Diretor' : 'Wachowski'}
              ]
print(locadora[0]) # Vai mostrar o filme na posição 0 
print(locadora[-1]) # Vai mostrar o ultimo filme da locadora
print(locadora[0]['Ano']) # Vai mostrar o ano de 1977 do filme star wars
print(locadora[1]['Diretor']) # Vai mostrar o diretor do filme avengers


# Outro exemplos 

pessoas = {}
pessoas = {'Nome' : 'Gustavo Guanabara', 'Sexo' : 'M', 'Idade' : 22}
print(pessoas)

pessoas = {}
pessoas = {'Nome' : 'Gustavo Guanabara', 'Sexo' : 'M', 'Idade' : 22}
print(f'{pessoas["Nome"]} vai ter {pessoas["Idade"]} Anos') # Aqui tem q usar aspas duplas para declara a chave .

# Usando laços 

pessoas = {}
pessoas = {'Nome' : 'Gustavo Guanabara', 'Sexo' : 'M', 'Idade' : 22}
for k in pessoas.keys():
    print(k) # Vai me mostrar as chaves : Nome, Sexo e Idade

for v in pessoas.values():
    print(v) # Vai me mostrar os valores : Gustavo Guanabara, M e 22

for k,v in pessoas.items():
    print(f'{k} = {v}') # Vai me mostrar as chaves e os valores correspondente.


pessoas = {}
pessoas = {'Nome' : 'Gustavo Guanabara', 'Sexo' : 'M', 'Idade' : 22}
del pessoas['Sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}') # Vai me mostrar as chaves e os valores correspondente.

pessoas = {}
pessoas = {'Nome' : 'Gustavo Guanabara', 'Sexo' : 'M', 'Idade' : 22}
pessoas['Peso'] = 99.5 # Vai adicionar a chave peso.
for k,v in pessoas.items():
    print(f'{k} = {v}') # Vai me mostrar as chaves e os valores correspondente.


# Dicionários dentro de lista.

brasil = []
estado1 = {'Uf' : 'Rio de Janeiro', 'Sigla' : 'RJ'}
estado2 = {'Uf' : 'São Paulo', 'Sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

brasil = []
estado1 = {'Uf' : 'Rio de Janeiro', 'Sigla' : 'RJ'}
estado2 = {'Uf' : 'São Paulo', 'Sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['Uf']) # Vai me mostrar Rio de Janeiro.

brasil = []
estado1 = {'Uf' : 'Rio de Janeiro', 'Sigla' : 'RJ'}
estado2 = {'Uf' : 'São Paulo', 'Sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['Sigla']) # Vai me mostrar SP.


# IMPORTANTE

estado = dict()
brasil = list()
for c in range (0,3):
    estado['UF'] = str(input('Digite Unidade Federativa : '))
    estado['Sigla'] = str(input('Digite a Sigla : '))
    brasil.append(estado) # Aqui vai criar uma relação do dicionario com a lista e não vai copiar todos os dados.

print(brasil)
# Vai dar erro

# JEITO CERTO

estado = dict()
brasil = list()
for c in range (0,3):
    estado['UF'] = str(input('Digite Unidade Federativa : '))
    estado['Sigla'] = str(input('Digite a Sigla : '))
    brasil.append(estado.copy()) # Aqui vou conseguir copiar os dados do meu dicionário para minha lista

print(brasil)

estado = dict()
brasil = list()
for c in range (0,3):
    estado['UF'] = str(input('Digite Unidade Federativa : '))
    estado['Sigla'] = str(input('Digite a Sigla : '))
    brasil.append(estado.copy()) # Aqui vou conseguir copiar os dados do meu dicionário para minha lista

for e in brasil : # Mostrando os estados da minha lista.
    for k,v in estado.items() : # Mostra minhas chaves e valores do dicionario estado
        print(f'O campo {k} tem o valor {v}')


