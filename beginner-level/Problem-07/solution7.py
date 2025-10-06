
input= [1, 2, 4, 5]

def find_missing_number(sequence):

    n = len(sequence) + 1  

    expected_sum = n * (n + 1) // 2  

    actual_sum = sum(sequence)  
    missing_number = expected_sum - actual_sum
      
    return missing_number   

logs = find_missing_number(input)
print("missing:", logs)
