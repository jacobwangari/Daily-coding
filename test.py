def are_equivalent(sentence1, sentence2, synonyms):
    words1 = sentence1.split()
    words2 = sentence2.split()

    if len(words1) != len(words2):
        return False

    mapping = {}
    for a, b in synonyms:
        if a not in mapping:
            mapping[a] = [a]
        if b not in mapping:
            mapping[b] = [b]
        mapping[a].append(b)
        mapping[b].append(a)

    for i in range(len(words1)):
        word1 = words1[i]
        word2 = words2[i]
        if word1 not in mapping or word2 not in mapping:
            return False
        if word2 not in mapping[word1]:
            return False

    return True

sentence1 = "He wants to eat food."
sentence2 = "He wants to consume food."
synonyms = [("eat", "consume")]
print(are_equivalent(sentence1, sentence2, synonyms)) # True
