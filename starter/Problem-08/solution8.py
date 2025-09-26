

def guess_number(guess):
    
    
    number=int(input("guess a number from 1 to 9: "))

    print(number)
    if number < guess:
        print("your guess is almost there")
    elif number > guess:
        print("your guess is higher")
    elif number == guess:
        print("your guess is correct")

guess_number(6)