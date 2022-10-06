from collections import defaultdict

# xyz 마트

def solution(want, number, discount):
    hm = defaultdict(int)


    for i in range(len(want)):
        hm[want[i]] = number[i]

    answer = 0
    for i in range(len(discount) - 9):
        dc = discount[i:i + 10]
        cnt = 0
        for w in want:
            if hm[w] == dc.count(w):
                cnt += 1
        if cnt == len(want):
            answer += 1
    return answer