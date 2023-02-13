# mapping is implemented using dictionary

#given list of tuples
synonyms = [("eat", "consume"), ("big", "large")]

#we can create a dictionary
mapping = {}
for a, b in synonyms:
    mapping[a] = b

print(mapping)


#map multiple values to a single key ~ json
synonyms = [("eat", "consume"), ("big", "large"), ("large", "huge")]
mapping = {}
for a, b in synonyms:
    if a not in mapping:
        mapping[a] = [a]
    if b not in mapping:
        mapping[b] = [b]
    mapping[a].append(b)
    mapping[b].append(a)

print(mapping)