def number_pattern(n):
    # Check if the input is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if the integer is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Generate the pattern using a for loop
    pattern_list = []
    for i in range(1, n + 1):
        pattern_list.append(str(i))
    
    # Return the numbers joined by a space
    return " ".join(pattern_list)
print(number_pattern(5))
