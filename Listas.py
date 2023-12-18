""" LISTAS """

# Variáveis Compostas
# Diferentemente das tuplas, as lista são mutáveis.
# Listas são representadas por = []
# EXEMPLO : 
# Lista = [] Ou Lista = list()

#Comando Append = Serve para adicionar elementos na minha lista, sempre vai adicionar no final da lista.
#Por exemplo : 
lanche = ['Hamburguer','Suco','Pizza','Picolé']
lanche.append('Cookie')
print(lanche)

#Comando Insert = Serve para adicionar elementos na minha lista, mas diferentemente do append, esse pode adicionar em qualquer posição que você pedir.
#Por exemplo : 
lanche = ['Hamburguer','Suco','Pizza','Picolé','Cookie']
lanche.insert(0,'Cachorro quente') # Vai adicionar na posição 0 o elemento 'Cachorro quente'. 
print(lanche)

# Comando del = Serve para deletar elementos da minha lista.
#Por exemplo :
lanche = ['Hamburguer','Suco','Pizza','Picolé','Cookie']
del lanche[3] # Vai deletar o picolé
print(lanche)

# Comando pop = Serve para deletar elementos da minha lista, se não passar nenhum parâmetro, vai deletar o ultimo elemento da lista.
#Por exemplo : 
lanche = ['Hamburguer','Suco','Pizza','Picolé','Cookie']
lanche.pop() # Sem parâmetro, vai deletar o ultimo elemento
print(lanche)

lanche = ['Hamburguer','Suco','Pizza','Picolé','Cookie']
lanche.pop(3) # Com parâmetro
print(lanche)

# Comando remove = Serve para deletar elementos da minha lista, mas a partir do valor.
#Por exemplo : 
lanche = ['Hamburguer','Suco','Pizza','Picolé','Cookie']
lanche.remove('Pizza') # Aqui coloco o valor contido na minha lista e não os indices.
print(lanche)

# Comando sort = Serve para por os elementos em ordem
#Por exemplo : 
valores = [8,2,5,4,9,3,0]
valores.sort() # Aqui vai ordenar em ordem crescente.
print(valores)

valores = [8,2,5,4,9,3,0]
valores.sort(reverse=True) # Aqui vai ordenar em ordem decrescente.
print(valores)

# Comando len = Serve para saber o tamanho da variável
#Por exemplo :
valores = [8,2,5,4,9,3,0]
tam = len(valores) 
print(tam) # Vai dizer o tamanho da lista valores.


# Parte prática.

num = [2,5,9,1]
num[2] = 3 
print(num)


valores = [] 
valores.append(5)
valores.append(8)
valores.append(9)
for c, v in enumerate(valores) : # Vai enumerar a minha lista com indices.
    print(f'{v} na posição {c}')



valores = [] 
for c in range (0,4):
    valores.append(int(input('Digite um valor : ')))


for c, v in enumerate(valores) : # Vai enumerar a minha lista com indices.
    print(f'{v} na posição {c}')


#Copiando listas

a = [2,3,4,7]
b = a # Cria uma ligação entre as listas.
print(f'Lista A : {a}')
print(f'Lista B : {b}')

a = [2,3,4,7]
b = a 
b[2] = 69 # Vai alterar as duas listas por que a gente fez uma ligação ai em cima.
print(f'Lista A : {a}')
print(f'Lista B : {b}') 

a = [2,3,4,7]
b = a[:] # Pegue todos os elementos de a, nesse caso não vai ter a ligação entre as duas listas.
b[2] = 69 
print(f'Lista A : {a}')
print(f'Lista B : {b}') 