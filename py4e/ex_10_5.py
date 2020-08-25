# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
lista = list()
dicionario = dict()
#h = list()

for line in handle:
    if "From:" in line:
        continue
    elif "From" in line:
        words = line.split()
        lista.append(words[5])
        #print(lista)
        #lista[0][0:2]


for hora in lista:
    h = hora[0:2]
    #print(h)
    dicionario[h] = dicionario.get(h, 0) + 1

#print(dicionario)
#print( sorted( [(k,v) for k,v in dicionario.items()]))

lista2 = list()
lista2 = sorted( [(k,v) for k,v in dicionario.items()])
#print(lista2)

for k,v in lista2:
    print(k,v)
