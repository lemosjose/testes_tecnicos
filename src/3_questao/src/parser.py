import json
import typing 

f = open('../dados.json', 'r')

dados = json.load(f)
n = 0
m = 0
M = 0 

for i in dados:
    if(i == 0):
        continue 
    else:
        m = m + i['valor']
        n = n + 1
media = m/n 
menor: float 

def retornaMaior(maior):
    for i in dados:
        if i['valor'] > maior:
            maior = i['valor']
    return maior 

def retornaMenor(menor):
    for i in dados:
        if i['valor'] < menor:
            menor = i['valor']
    return menor


print(f"o maior valor é {retornaMaior(0)}")
print(f"o menor valor é {retornaMenor(retornaMaior(0))}")
print(f"a média dos valores é {media}")

