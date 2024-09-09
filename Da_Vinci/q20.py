def f(x):
    return (x**11 - 1) / (x - 1)
def f2(x):
    ans = 0
    for i in range(11):
        ans += x**i
    return ans

# f2(x) < 1- 
# print(f(x))
x = 5
print(f2(x) < 10**7)