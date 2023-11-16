def count_vowels(s):
    # Define the vowels
    vowels = "aeiou"

    # Initialize a dictionary to count each vowel
    vowel_count = {}

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char.lower() in vowels:
            # Convert to lowercase and count the vowel
            char = char.lower()
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1

    # Return the result
    if not vowel_count:
        return 'none'
    else:
        return vowel_count

# Example usage
input_string = input("Enter a string: ")
print(count_vowels(input_string))
