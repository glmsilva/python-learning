par = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        par = par+1
    else:
        continue

print(par,"valores pares")
