def reverse_string(s):
    if len(s) == 0:  # Base case: if the string is empty, return an empty string
        return s
    else:
        # Recursively call the function with the substring except the first character
        # and append the first character to the result
        return reverse_string(s[1:]) + s[0]

# Example usage
input_string = "inefficient"
reversed_string = reverse_string(input_string)
print(reversed_string)
