from itertools import combinations
foods = [1,2,3,0,3]
n = len(foods)

s = list(combinations(foods,3))
print(s)