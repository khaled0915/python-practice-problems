def flatten_json(nested_dict, parent_key='', sep='.'):
    
    flat_dict = {}
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, new_key, sep=sep))
        else:
            flat_dict[new_key] = value
    return flat_dict



nested = {"a": {"b": 1}}
flat = flatten_json(nested)
print(flat)
