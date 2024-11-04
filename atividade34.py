# Ler uma lista de 5 números inteiros e
# mostre cada número juntamente com a
# sua posição na lista.

lista = []

for i in range(1,6):
    numero = int(input("Digite o número: "))
    lista.append(numero)
for i, p in enumerate(lista):
    print(f" O número  {p} está na posição  {i + 1} ° da lista")