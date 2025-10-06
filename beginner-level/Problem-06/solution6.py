

def capitalize_words(text):
    words = text.split() 
    result = []
    for word in words:
        if len(word) > 0:
            result.append(word[0].upper() + word[1:].lower())  
        else:
            result.append(word)
    return " ".join(result)


sentence = "python for web developers"
print(capitalize_words(sentence)) 
