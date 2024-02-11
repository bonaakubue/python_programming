# Built-in methods for string
name = 'John'

#lower
print(name.lower())


#upper
print(name.upper())

#capitalize
print(name.capitalize())

#title
sentence = 'how are you doing?'
print(sentence.title())

#strip
word = '  hello '
print(word.strip())

#split
sentence = 'how are you doing?'
print(sentence.split())

#join
words = ' '.join(['hello', 'there']) 
print(words)

#isdigit
nums = '1234'
print(nums.isdigit())

nums = '12 Hillview'
print(nums.isdigit())

#isalpha
word = 'hello'
print(word.isalpha())

nums = '1234'
print(nums.isalpha())

#islower
word = 'hello'
print(word.islower())

word = 'HELLO'
print(word.islower())

#isupper
word = 'hello'
print(word.isupper())

word = 'HELLO'
print(word.isupper())
