


rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'


text = rhyme.lower()

freq = {}
for char in text:
    if char != " ":  
        freq[char] = freq.get(char, 0) + 1


most_frequent = max(freq, key=freq.get)

print("Most frequent character:", most_frequent) # t
print("Frequency:", freq[most_frequent]) # 6