# In operator

text="anubhav"
result= "a " in text # it also see space

print(result)

#unpacking in list

arr=[12,333,434]
a,b,c=arr
print(a)

#rest unpacking

a,*b=arr
print(b)

#Tuple 

tuple=(1,2,3)
a,b,c=tuple
print(a)
# in tuple we can not change the value or add or delete

# tuple.remove(2)
# print(tuple)
tu=tuple
tu+=(4,5)
tuple+=(4,5)
print(tuple)
#we can access value of tuple like array or list in python

#Dictionary

dict6={"name":"anubhav","age":20}
print(dict6)
print(dict6["name"])
print(dict6.get("name"))

# nested dictionary
dict1={
    "name":"anubhav",
    "age":20,
    "address":{
        "city":"kolkata",
        "state":"west bengal"
    }
}
print(dict1["address"]["city"])

#using a List a Tuples
# Convert a list of tuples to a dictionary
tuplelist = [(1, 2), (3, 4), (5, 6)]
tupledis = dict(tuplelist)  # Ensure dict() is used correctly
print(tupledis)

for key in tupledis:
    print(f"{key}: {tupledis[key]}")

# iterating through items

for key, value in tupledis.items():
    print(f"{key}: {value}")
\
#adding new key value pair

tupledis["newkey"] = "newvalue"
print(tupledis)
#updating dictionary
updatedtupledis={
    "name":"anubhav",
    "age":20,}

tupledis.update(updatedtupledis) 

print(tupledis)  