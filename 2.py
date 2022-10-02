from itertools import combinations
s = "abcd"

def isGoodString(str):
    exclude = []
    for i in range(len(pos)):
        if pos[i] in exclude:
            return False
        exclude.append(pos[i])
    return True

answer = set()
for i in range(len(s)):
    poss = s[i:]
    for j in range(i, len(s)+2):
        pos = poss[:j-1]
        print(pos)
        if len(pos) == 0: continue
        if len(pos) == 1:
            answer.add(pos)
        else:
            if isGoodString(pos):
                answer.add(pos)

