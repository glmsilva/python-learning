n = int(input())
x = list()

menor = None



if n > 1 and n < 1000:

    x = input().split()

    for i in range(n):
        if menor is None:
            menor = int(x[i])
        elif menor > int(x[i]):
            menor = int(x[i])

    print("Menor valor:", menor)
    print("Posicao:", x.index(str(menor)))
