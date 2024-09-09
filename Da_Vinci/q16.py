targets = [33, 45, 47, 57, 69, 70]
denoms = [13, 17, 22]
import math
a_max = math.floor(max(targets) / denoms[0])
b_max = math.floor(max(targets) / denoms[1])
c_max = math.floor(max(targets) / denoms[2])

ans = []
for a in range(a_max+1):
    for b in range(b_max+1):
        for c in range(c_max+1):
            x =  a * denoms[0] + b * denoms[1] + c * denoms[2] 
            if x in targets:
                if x not in ans:
                    ans.append(x)
                    print(x, a, b, c)


print('count', len(ans))