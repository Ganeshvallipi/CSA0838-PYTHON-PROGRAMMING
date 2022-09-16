def anagram_check(keywords):
    anagrams=defauldict(list)
    for i in keywords:
        histogram=tuple(counter(i).items())
        anagrams[histogram].append(i)
        return list(anagrams.values())
    keywords=("banana")
    print(anagram_check(keywords))
