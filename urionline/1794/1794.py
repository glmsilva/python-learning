n = int(input())
lavadeira = list()
secadora = list()

lavadeira = input().split()
secadora = input().split()

la = int(lavadeira[0])
lb = int(lavadeira[1])
sa = int(secadora[0])
sb = int(secadora[1])

pos_l = False
pos_s = False

if n <= 100:
    if la >= 1 and la <= 100:
        if lb <= 100 and lb > la:
            if n >= la and n <= lb:
                pos_l = True

    if sa >= 1 and sa <= 100:
        if sb <= 100 and sb > sa:
            if n >= sa and n <= sb:
                pos_s = True

if pos_l and pos_s:
    print("possivel")
else:
    print("impossivel")
