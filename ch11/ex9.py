#generator function
def num_gen(n):
    for i in range(n):
        yield i

gen = num_gen(5)
for num in gen:
    print(num)

# iter() and next()
gen = num_gen(3)
iter1 = iter(gen)
print(next(iter1)) 
print(next(iter1)) 

#generating even numbers
def even_numbers(n):
    i = 0
    while i < n:
        yield i
        i += 2

gen = even_numbers(10)
for num in gen:
    print(num)
