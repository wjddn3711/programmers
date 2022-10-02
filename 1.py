v = [[1,4],[3,4],[3,10]]
xs = []
ys = []
for x, y in v:
    if x in xs: xs.remove(x)
    else: xs.append(x)
    if y in ys: ys.remove(y)
    else: ys.append(y)

answer = [xs[0], ys[0]]
print(answer)