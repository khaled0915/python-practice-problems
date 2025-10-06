
text="Data Science is awesome"

lower_text= text.lower()

vowel ='aeiou'
count=0

for char in lower_text:
    if char in vowel:
        count += 1

        
print("Number of vowels:", count)