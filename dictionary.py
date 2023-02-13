myDict = {'ten' : 10, 'twenty' : 20, 'thirty' : 30, 'forty' : 40}
print(myDict)

#keys() returns the keys of the dictionary
print(list(myDict.keys()))

#values() returns the values of the dictionary
print(list(myDict.values()))

#items() return the items using (key, value) pairs format.
print(list(myDict.items()))

# len() returns number of elements in dictionary
print(len(myDict))

# dictionary[key] returns item with the key
print(myDict['ten'])

myDict.update({'fifty' : 50})
print(myDict)

#iter(d) - return an iterator over the keys of dictionary
items = iter(myDict)
for i in range(len(myDict)):
    item = next(items)
    print(item)



# myDict.update({'fifty' : 50})
# print(myDict)