def first_recurring("given_string"):
    counts = {} // dictionary or hash_table
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char] = 1
            return none
