"""
This problem was asked by Google.

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?

"""
#my solution

def are_equivalent(sentence1, sentence2, synonyms):
    words1 = sentence1.split()
    #print(words1)
    words2 = sentence2.split()
    #print(words2)

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

    #print(mapping)

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
synonyms = [("eat", "consume"), ("big", "large")]


test = are_equivalent(sentence1, sentence2, synonyms)
print(test)
