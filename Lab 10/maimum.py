def max_product(tuple_elements):
    """Return the maximum product of any two distinct elements in the tuple."""

    # Initialize the two largest distinct elements
    max1 = max2 = float('-inf')

    for number in tuple_elements:
        if number > max1:
            # Update the two largest elements
            max2 = max1
            max1 = number
        elif max1 > number > max2:
            max2 = number

    # Check if max2 has been updated, indicating a second distinct element was found

    return max1 * max2

# Example usage
tuple_elements = tuple(map(int, input().strip('()').split(',')))
print("Maximum product:", max_product(tuple_elements))
