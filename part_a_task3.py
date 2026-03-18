# Part A - Task 3
# Convert list of tuples to dictionary and find key with highest value

def tuples_to_dict(tuple_list):
    result = {}
    for item in tuple_list:
        key = item[0]
        value = item[1]
        result[key] = value
    return result


def key_with_max_value(d):
    max_key = None
    max_val = None
    for key in d:
        if max_val is None or d[key] > max_val:
            max_val = d[key]
            max_key = key
    return max_key


# --- Testing ---
tuple_list = [("a", 10), ("b", 45), ("c", 23), ("d", 67), ("e", 5)]

my_dict = tuples_to_dict(tuple_list)
print("Tuple list:", tuple_list)
print("Converted dict:", my_dict)

top_key = key_with_max_value(my_dict)
print("Key with highest value:", top_key)
