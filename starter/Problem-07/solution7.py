def num(a):
    if a%3 == 0:
        print("fizz")

    elif a%5 == 0:
        print("buzz")

    elif a%3 == 0 and a%5 == 0:
        print("fizzbuzz")   
    else:
        print("not a fizz-buzz number")

num(9) # fizz
num(10) # buzz
num(15) # fizzbuzz
num(7) # not a fizz-buzz number