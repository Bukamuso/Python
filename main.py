
# Import your module
import rectangle_utils

# Ask the user for input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = rectangle_utils.calculate_area(length, width)
perimeter = rectangle_utils.calculate_perimeter(length, width)

# Display results
print(f"\nThe area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
