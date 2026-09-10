dictionary={"India":"New Delhi","Netherlands":"Amsterdam","U.S.A":"Washington D.C"}
print(dictionary["U.S.A"])
print(len(dictionary))
dictionary["Japan"]="Tokyo"
print(dictionary)
del dictionary["U.S.A"]
print(dictionary)
for key in dictionary:
    print(key)
for key in dictionary.keys():
    print(key)
for value in dictionary.values():
    print(value)
for key,value in dictionary.items():
    print(key,value)