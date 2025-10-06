
def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        key = ''.join(sorted(word)) 
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    return list(anagram_dict.values())



words = ["bat", "tab", "cat", "act"]
print(group_anagrams(words))
