from pprint import pprint
dicr = []
n = 16

for a in range(n):
    b = {'bin': bin(a), 'dec': a, 'hex': hex(a), 'oct': oct(a)}
    dicr.append(b)

pprint(dicr)
