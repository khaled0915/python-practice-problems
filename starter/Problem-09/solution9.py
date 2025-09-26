my_list = [4, 8, 7, 4, 3, 6, 2, 1, 9]

#sol-01
# for item in my_list:
#     if item == 6:
#         print("found 6")
#         break
# else:
#     # This else belongs to the for loop (runs only if no break happens)
#     print("6 is not in the list")


#sol-02
if 6 in my_list:
    print("found 6")
else:
    print("6 is not in the list")
        
        