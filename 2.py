# type of
x=True
print(type(x)) 

# python provide typecasting
y=10.7
print(type(y))
print(int(y))# to convert to int similarly we can use others.

# int,float,str,bool we can use this

# string methods

# uppercase & lowercase
text="hello"
print(text.upper()) # here we have to call function 
print(text.lower()) 
print(text.capitalize()) # to captical the first letter
print(text.title()) # to capital after space first letter.


# str.strip , str.lstrip, and str.rstrip
sentence = "  python is fun   "
print(sentence.strip()) # to trim
print(sentence.lstrip()) # to trim left side
print(sentence.rstrip()) # to trim right side

#str.startswith (prefix) and str.endswith (suffix)

print(sentence.startswith("  python")) # it also include spaces

print(sentence.replace('python','javascript'))
print(sentence.find('python')) #index of 2 python is present similarly we can use sentence.index

print (sentence.split()) # split in array 

print(sentence.count("p"))







