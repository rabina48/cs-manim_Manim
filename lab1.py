# Open the file
# file = open('file.txt', 'r')

# # Read the lines into a list
# lines = []
# for line in file:
#     lines.append(line.strip().split(' '))

# # Close the file
# file.close()

# # Prepare to transpose the list
# transposed = []
# for i in range(len(lines[0])):  # Assuming all rows have the same number of columns
#     # Collect the ith element of each row
#     transposed_row = []
#     for row in lines:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# # Print the transposed content
# for row in transposed:
#     print(' '.join(row))


#--------2-----

# # Function to check if an email address is valid
# def is_valid_email(email):
#     # Check for one '@' symbol
#     if email.count('@') != 1:
#         return False
#     # Split the email into local and domain parts
#     local, domain = email.split('@')
#     # Check for at least one '.' in the domain part
#     if '.' not in domain:
#         return False

#     # Check if the top-level domain is at least two characters long
#     if len(domain.split('.')[-1]) < 2:
#         return False

#     # Check for valid characters in the local part
#     for char in local:
#         if not (char.isalnum() or char in ['.', '+']):
#             return False

#     # Check for valid characters in the domain part
#     for char in domain:
#         if not (char.isalnum() or char == '.'):
#             return False
#     return True
# # Initialize a counter for valid emails
# valid_count = 0
# # Open and read the file
# with open('file.txt', 'r') as file:
#     for line in file:
#         # Check if the email is valid
#         if is_valid_email(line.strip()):
#             valid_count += 1

# # Print the count of valid emails
# print(valid_count)

# 2nd part
# Function to check if an email address is valid
# def is_valid_email(email):
#     # Check for one '@' symbol
#     if email.count('@') != 1:
#         return False
    
#     # Split the email into local and domain parts
#     local, domain = email.split('@')
    
#     # Check if the local part is empty
#     if not local:
#         return False
    
#     # Check for at least one '.' in the domain part
#     if '.' not in domain:
#         return False

#     # Check if the top-level domain is at least two characters long
#     if len(domain.split('.')[-1]) < 2:
#         return False

#     # Check for valid characters in the local part
#     for char in local:
#         if not (char.isalnum() or char in ['.', '+']):
#             return False

#     # Check for valid characters in the domain part
#     for char in domain:
#         if not (char.isalnum() or char == '.'):
#             return False
            
#     return True

# # Initialize a counter for valid emails
# valid_count = 0

# # Open and read the file
# with open('file.txt', 'r') as file:
#     for line in file:
#         # Check if the email is valid
#         if is_valid_email(line.strip()):
#             valid_count += 1

# # Print the count of valid emails
# print(valid_count)


#Luckey

# def findLuckeyIndex(nums):
#     # Iterate through each index of the array
#     for i in range(len(nums)):
#         # Calculate the sum of numbers to the left and right of the current index
#         left_sum = sum(nums[:i])
#         right_sum = sum(nums[i+1:])

#         # Check if the left sum is equal to the right sum
#         if left_sum == right_sum:
#             # Return the current index if it's a valid middleIndex
#             return i

#     # Return -1 if no valid middleIndex is found
#     return -1

# # Test the function with provided examples
# print(findLuckeyIndex([2,3,-1,8,4]))  # Output: 3
# print(findLuckeyIndex([1,-1,4]))      # Output: 2
# print(findLuckeyIndex([2,5]))         # Output: -1



# # set list array
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

# Function to check if an email address is valid
# def is_valid_email(email):
#     # Check for one '@' symbol
#     if email.count('@') != 1:
#         return False
    
#     # Split the email into local and domain parts
#     local, domain = email.split('@')
    
#     # Check if the local part is empty
#     if not local:
#         return False
    
#     # Check for at least one '.' in the domain part
#     if '.' not in domain:
#         return False

#     # Check if the top-level domain is at least two characters long
#     if len(domain.split('.')[-1]) < 2:
#         return False

#     # Check for valid characters in the local part
#     for char in local:
#         if not (char.isalnum() or char in ['.', '+']):
#             return False

#     # Check for valid characters in the domain part
#     for char in domain:
#         if not (char.isalnum() or char == '.'):
#             return False
            
#     return True

# # Prompt the user for the number of email addresses they want to input
# n = int(input())

# # Open a file in write mode to store valid email addresses
# with open('file.txt', 'w') as valid_file:
#     # Initialize a counter for valid emails
#     valid_count = 0

#     # Loop to input 'n' email addresses from the user
#     for i in range(n):
#         email = input()

#         # Check if the email is valid
#         if is_valid_email(email):
#             valid_count += 1
#             # Write valid email addresses to the file
#             valid_file.write(email + '\n')

# # Print the count of valid email addresses
# print(f"Number of valid email addresses: {valid_count}")


def subsets(nums):
    def backtrack(start, current):
        # Add the current subset to the result
        result.append(current[:])

        # Iterate over the numbers to build subsets
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current.append(nums[i])
            # Move on to the next element
            backtrack(i + 1, current)
            # Exclude nums[i] from the current subset for backtracking
            current.pop()

    result = []
    backtrack(0, [])
    return result

# Prompt the user for the number of elements in the set
n = int(input("Enter the number of elements in the set: "))

# Prompt the user to enter the elements one by one
nums = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    nums.append(num)

# Find and print the subsets
subsets_result = subsets(nums)
print("Subsets:")
for subset in subsets_result:
    print(subset)






