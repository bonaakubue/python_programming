# Operations on sets

#union
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7,8}
result = S1.union(S2)
print(result)

# alternatively
result = S1 | S2
print(result)


#intersection
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7,8}

result = S1.intersection(S2)
print(result)

# alternatively
result = S1 & S2
print(result)


#difference
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7,8}
result = S1.difference(S2)
print(result)


result = S1 - S2
print(result)

result = S2.difference(S1)
print(result)

#alternatively
result = S2 - S1
print(result)

#symmetric difference
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7,8}

result = S1.symmetric_difference(S2)
print(result)

#alternatively
result = S1 ^ S2
print(result)
