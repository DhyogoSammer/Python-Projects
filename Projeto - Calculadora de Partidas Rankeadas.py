## Objetivo 

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, 
# Depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito 
# Através do calculo ( vitorias - derrotas )

# Se as vitorias forem menores que 10 = Ferro
# Se as vitorias forem entre 11 e 20 = Bronze 
# Se as vitorias forem entre 21 e 50 = Prata
# Se as vitorias forem entre 51 e 80 = Ouro 
# Se as vitorias forem entre 81 e 90 = Diamante 
# Se as vitorias forem entre 91 e 100 = Lendário
# Se as vitorias for maior ou igual a 101 = Imortal

## Saida 

# O Heroi tem de saldo {saldovitorias} e está no nivel {nivel}


def calc(vit,der):
    saldo = vit - der 
    if vit <= 10 :
        return f'O Heroi tem de saldo {saldo} e está no nível de Ferro'
    elif vit > 10 and vit <= 20:
        return f'O Heroi tem de saldo {saldo} e está no nível de Bronze'
    elif vit > 21 and vit <= 50:
        return f'O Heroi tem de saldo {saldo} e está no nível de Prata'
    elif vit > 51 and vit <= 80:
        return f'O Heroi tem de saldo {saldo} e está no nível de Ouro'
    elif vit > 81 and vit <= 90:
        return f'O Heroi tem de saldo {saldo} e está no nível de Diamante'
    elif vit > 91 and vit <= 100:
        return f'O Heroi tem de saldo {saldo} e está no nível de Lendário'
    else :
        return f'O Heroi tem de saldo {saldo} e está no nível de Imortal'





vitorias_derrotas = calc(int(input('Vitorias : ')), int(input('Derrotas : ')))
print(vitorias_derrotas)