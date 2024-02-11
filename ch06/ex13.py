# String substitution methods
# Format function
S = '{} shirts in the {} box'.format(5, 'blue')
print(S)

S = '{0} shirts in the {1} box'.format(5, 'blue')
print(S)

S = '{1} shirts in the {0} box'.format(5, 'blue')
print(S)

# F-strings
box = 'blue'
S = f'There are {2+3} shirts in the {box} box'
print(S)

# Old String Substitution
S = '%s oranges' % 5
print(S)

S = '%s shirts in the %s box' % (5, 'blue')
print(S)
