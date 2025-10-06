

text=input("enter a string :")
reversed_text=""

for i in range(len(text)-1,-1,-1):
    reversed_text+=text[i]

print("reversed text:", reversed_text)