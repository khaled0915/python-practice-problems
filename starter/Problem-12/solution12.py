

from operator import index


list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]

common_elements =[]

for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)
print("common Elements : ", common_elements) # [4, 7, 8]

def sum_of_common_elements(common_elements):
    return sum(common_elements)
print("Sum of common Elements : ", sum_of_common_elements(common_elements)) # 19