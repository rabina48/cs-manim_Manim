# with open("data_file.txt") as f:
#     content_list = f.readlines()

# # print the list
# print(content_list)

# # remove new line characters
# content_list = [x.strip() for x in content_list]
# print(content_list)

## For Transpose

# Read the file and store the data in a list of lists
# with open('file.txt', 'r') as file:
#     lines = [line.strip().split(' ') for line in file]

# # Transpose the data using zip
# transposed_data = zip(*lines)

# # Convert the transposed data back into formatted strings and print them
# for row in transposed_data:
#     print(' '.join(row))


## Tenth line

# with open('file.txt', 'r') as file:
#     for i, line in enumerate(file, start=1):
#         if i == 10:
#             print(line.strip())
#             break
#     else:
#         print("Less than 10 lines in the file")


# N = int(input("Enter the number of strings: "))
 
# # Open file for writing
# with open("file.txt", "w") as f:
#     # Insert the strings into file
#     for i in range(N):
#         name = input("Enter the string: ")
#         # Writing into the file
#         f.write(name + "\n")
 
# # Open file for reading
# with open("file.txt", "r") as f:
#     # Read the lines until end of file is reached
#     names = [line.strip() for line in f.readlines()]
 
# # Sort the strings
# names.sort()
 
# # Open the file for writing
# with open("file1.txt", "w") as f:
#     # Insert the sorted strings into the file
#     for name in names:
#         f.write(name + "\n")
 
# # Print the sorted names
# for name in names:
#     print(name)

## EMail
# import re

# def is_valid_email(email):
#     # Define the email validation regex pattern
#     pattern = r'^[a-zA-Z0-9.+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

# def count_valid_emails(file_name):
#     valid_count = 0
#     with open(file_name, 'r') as file:
#         for line in file:
#             email = line.strip()
#             if is_valid_email(email):
#                 valid_count += 1
#     return valid_count

# # Replace 'file.txt' with your actual file name
# print(count_valid_emails('file.txt'))

# #geeks
# def sort_strings_in_file(file_name):
#     with open(file_name, 'r') as file:
#         # Read lines and remove newline characters
#         strings = [line.strip() for line in file]

#     # Sort the strings
#     strings.sort()

#     # Return the sorted list
#     return strings

# # Replace 'file.txt' with your actual file name
# sorted_strings = sort_strings_in_file('file.txt')

# # Print the sorted list in the specified format
# print(sorted_strings)


## set list array
# def subsets(nums):
#     def backtrack(start, current):
#         # Add the current subset to the result
#         result.append(current[:])

#         # Iterate over the numbers to build subsets
#         for i in range(start, len(nums)):
#             # Include nums[i] in the current subset
#             current.append(nums[i])
#             # Move on to the next element
#             backtrack(i + 1, current)
#             # Exclude nums[i] from the current subset for backtracking
#             current.pop()

#     result = []
#     backtrack(0, [])
#     return result

# # Example usage
# nums = [1, 2, 3]
# print(subsets(nums))


# Open the file
# file = open('file.txt', 'r')

# # Initialize a variable to keep track of line numbers
# line_number = 0

# # Initialize an empty list to store the lines
# even_index_lines = []

# # Loop through each line in the file
# for line in file:
#     # Check if the current line number is even
#     if line_number % 2 == 0:
#         # Append the line (without the newline character) to the list
#         even_index_lines.append(line.strip())

#     # Increment the line number by 1
#     line_number += 1

# # Close the file
# file.close()

# # Print the list of lines at even indices
# print(even_index_lines)


##Last

# # Prompt the user for the number of lines they want to input
# n = int(input("Enter the number of lines: "))

# # Open the file in write mode ('w') to overwrite any existing content
# file = open('file.txt', 'w')

# # Initialize an empty list to store the lines
# lines = []

# # Loop to input 'n' lines from the user and write them to the file
# for i in range(n):
#     line = input(f"Enter line {i + 1}: ")
#     lines.append(line)

# # Write the lines to the file, each on a separate line
# file.write('\n'.join(lines))

# # Close the file
# file.close()

# # Open the file in read mode ('r')

# file = open('file.txt', 'r')

# # Initialize a variable to keep track of line numbers
# line_number = 0

# # Initialize an empty list to store the lines
# even_index_lines = []

# # Loop through each line in the file
# for line in file:
#     # Check if the current line number is even
#     if line_number % 2 == 0:
#         # Append the line (without the newline character) to the list
#         even_index_lines.append(line.strip())

#     # Increment the line number by 1
#     line_number += 1

# # Close the file
# file.close()

# # Print the list of lines at even indices
# print("Lines at even indices:")
# for line in even_index_lines:
#     print(line)

# Prompt the user for the number of lines they want to input
n = int(input("Enter the number of lines: "))

# Open the file in write mode ('w') to overwrite any existing content
file_name = 'file.txt'
with open(file_name, 'w') as file:
    # Initialize an empty list to store the lines
    lines = []

    # Loop to input 'n' lines from the user and write them to the file
    for i in range(n):
        line = input(f"Enter row {i + 1} data (space-separated): ")
        file.write(line + '\n')  # Write the line to the file
        lines.append(line)

# Split the lines into columns and transpose the content
transposed_data = []
for line in lines:
    columns = line.split()
    transposed_data.append(columns)

# Transpose the data using zip
transposed_data = list(map(list, zip(*transposed_data)))

# Print the transposed content
for row in transposed_data:
    print(' '.join(row))



