arq_nome = input("Enter file name: ")
arquivo = open(arq_nome)

lista = list()

for linha in arquivo :
    linha = linha.split()
    for palavra in linha:
        if lista.count(palavra) > 0:
            continue
        else:
            lista.append(palavra)

lista.sort()
print(lista)
