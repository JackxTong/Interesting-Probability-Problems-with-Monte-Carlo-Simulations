A, B = [], []
for i in range(100, 1000):
    digits = str(i)
    if int(digits[0]) + int(digits[1]) == int(digits[2]):
        A.append(digits)
    if int(digits[0]) + int(digits[1]) == 2 * int(digits[2]):
        B.append(digits)

print(len(A), len(B))