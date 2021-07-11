sentence = "The quick brown fox jumped over the lazy dog"

vowels = frozenset("aeiou")

finalSet = set(sentence).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
