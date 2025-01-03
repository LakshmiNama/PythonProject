# Strings

name = "Lakshmi"
print(type(name))
print(name)
print(name.upper())
print(name.lower())
print(len(name))

a = "90"
age = 90
print(type(a))
print(type(age))

name = "I work for Accenture"
# name = name + 1 - it gives error. As u canot add str with int
name = name + str(1) # change 1 to string
print(name)

# CONCAT

first_name = "Lakshmi"
last_name = "Sharath"
full_name = first_name + last_name
print(full_name)

how_many_cars_i_have = None
print(type(how_many_cars_i_have))   #None Type

# Null is not present in python

# id

age = 10
age2 = 10
age1 = 15

print(id(age))
print(id(age2))
print(id(age1))

