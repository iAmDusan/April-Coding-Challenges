def length_of_last_word(s):
    # Step 1: Trim the string to remove leading and trailing spaces.
    trimmed_string = s.strip()
    
    # Step 2: Split the string into words by spaces.
    words = trimmed_string.split()
    
    # Step 3: Get the last word in the list of words.
    last_word = words[-1]
    
    # Step 4: Return the length of the last word.
    return len(last_word)

# Example usage:
s1 = "Hello World"
print(length_of_last_word(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(length_of_last_word(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(length_of_last_word(s3))  # Output: 6
