import re

file = open("regex_sum_903867.txt")
numeros = list()
for line in file:
    if re.findall('[0-9]+', line):
        l = re.findall('[0-9]+', line)
        for num in l:
            numeros.append(num)


#print(numeros)
soma = None
for num in numeros:
    if soma is None:
        soma = int(num)
    else:
        soma += int(num)

print(soma)

#short solution
#Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
