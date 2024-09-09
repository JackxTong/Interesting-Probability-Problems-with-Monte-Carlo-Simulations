def find_triplets(a, b):
    solutions = []
    
    # Iterate over possible values of z
    for z in range(1, a):  # Since x, y, z are positive integers
        # Iterate over possible values of y
        for y in range(1, a - z):
            # Solve for x using the first equation: x + y + z = a
            x = a - y - z
            
            # Check if x is positive and satisfies the second equation
            if x > 0 and x + 2*y + 3*z == b:
                solutions.append((x, y, z))
    
    return solutions

# Example usage:
a = 100
b = 200
triplets = find_triplets(a, b)
print("Triplets (x, y, z) that satisfy the equations:")
print(len(triplets))
# for triplet in triplets:
    # print(triplet)
