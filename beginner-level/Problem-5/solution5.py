input = [1, [2, 3], [4, [5]]]

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

flattened = flatten(input)
print("flattened:", flattened)