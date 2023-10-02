import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and perimeter (circumference)
area = math.pi * (radius**2)
perimeter = 2 * math.pi * radius

# Display the results
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")
