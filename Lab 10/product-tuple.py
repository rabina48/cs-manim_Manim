# def tupleSameProduct(nums):
#     product_count = {}
#     total_tuples = 0

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             product = nums[i] * nums[j]

#             # If the product is already in the dictionary, it means we have found
#             # another pair that gives the same product. We add 8 times the current
#             # count of this product to the total, as each new pair with the same
#             # product can form 8 different tuples with all previous pairs.
#             if product in product_count:
#                 total_tuples += 8 * product_count[product]

#             # Count the occurrence of each product
#             if product in product_count:
#                 product_count[product] += 1
#             else:
#                 product_count[product] = 1

#     return total_tuples

# # Example usage
# nums = list(map(int, input("Enter the elements separated by space: ").split()))
# print("Number of valid tuples:", tupleSameProduct(nums))



# def tupleSameProduct( nums):
#     count = 0
#     seen = {}
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             prod = nums[i] * nums[j]
#             if prod in seen:
#                 count += seen[prod]
#                 seen[prod] += 1
#             else:
#                 seen[prod] = 1
        
#     return count * 8


# input_tuple = tuple(map(int, input("Enter space-separated integers for the tuple: ").split()))

# # Call the function with the input tuple
# result = tupleSameProduct(input_tuple)

def tupleSameProduct(nums):
    count = 0
    seen = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            prod = nums[i] + nums[j]
            if prod in seen:
                count += seen[prod]
                seen[prod] += 1
            else:
                seen[prod] = 1
        
    return count * 4

# Taking user input and converting it to a tuple of integers
user_input = input("Enter the elements separated by space: ")
nums_tuple = tuple(map(int, user_input.strip('()').split(',')))

# Call the function with the user-provided tuple
print("Number of valid tuples:", tupleSameProduct(nums_tuple))


