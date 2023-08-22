#definir a quantidade de linhas e colunas das matrizes
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

#garante que o número de colunas e linhas sejam iguais
while colunas!=linhas:
    print('Número de colunas deve ser igual ao número de linhas, digite novamente:')
    colunas = int(input("Digite o número de colunas: "))

#inicializar as matrizes vazias
matriz1 = []
matriz2 = []

#preencher a primeira matriz
for _ in range(linhas):
    linha = []
    for _ in range(colunas):
        elemento = int(input("Digite um elemento para a matriz 1: "))
        linha.append(elemento)
    matriz1.append(linha)

#exibir a matriz 1
print('Matriz 1:')
for exibirM1 in matriz1:
    print(exibirM1)

#preencher a segunda matriz
for _ in range(linhas):
    linha = []
    for _ in range(colunas):
        elemento = int(input("Digite um elemento para a matriz 2: "))
        linha.append(elemento)
    matriz2.append(linha)

#exibir a matriz 2
print('Matriz 2:')
for exibirM2 in matriz2:
    print(exibirM2)

#inicializar a matriz de soma com zeros
matriz_soma = []
for _ in range(linhas):
    linha = []
    for _ in range(colunas):
        linha.append(0)
    matriz_soma.append(linha)

#somando as matrizes
for i in range(linhas):
    for j in range(colunas):
        matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

#imprimir a matriz de soma
print("Soma das matrizes:")
for linha in matriz_soma:
    print(linha)