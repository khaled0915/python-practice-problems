import string
from collections import Counter

def most_frequent_word(text, stopwords=None):
    if stopwords is None:
        stopwords = {"the", "is", "in", "and", "to", "a", "of", "it", "on", "for"}

   
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [word for word in words if word not in stopwords]

    counter = Counter(words)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None


blog_content = """
Python is a powerful programming language. It is widely used in data science, web development,
and automation. Python allows developers to write clean and readable code.
"""

print("most frequent word:", most_frequent_word(blog_content))
