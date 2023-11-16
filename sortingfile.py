# Prompt the user for the number of strings they want to input
n = int(input("Enter the number of strings: "))

# Open the file in write mode ('w') to overwrite any existing content
file_name = 'file.txt'
with open(file_name, 'w') as file:
    # Initialize an empty list to store the strings
    strings = []

    # Loop to input 'n' strings from the user and write them to the file
    for i in range(n):
        string = input(f"Enter string {i + 1}: ")
        file.write(string + '\n')  # Write the string to the file
        strings.append(string)

# Sort the strings alphabetically
strings.sort()

# Print the sorted list in the specified format
formatted_list = "[" + ", ".join(strings) + "]"
print(formatted_list)
