# Cartesian product of sets

S1 = {1,2,3}
S2 = {4,5,6}
P = {(x,y) for x in S1 for y in S2}
print(P)

# Cartesian product using simple iteration
S1 = {1,2,3}
S2 = {4,5,6}
P = []
for x in S1:
	for y in S2:
	    P.append((x,y))

print(P)

from itertools import product 
S1 = {1,2,3}
S2 = {4,5,6}
P = product(S1, S2)
print(set(P))
