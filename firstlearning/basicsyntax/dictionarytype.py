# dictionary research

person = {"name": "dwx", "age": 18}

person["sex"] = "male"  # add an element
print(person)
del person["age"]  # del an element
print(person)
person["sex"] = "female"  # change an element
print(person)
person.clear()  # clean all the elements
print(person)
del person
# print(person) raise error
