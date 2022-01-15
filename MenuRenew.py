from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(course)):
        a = [] # n개 코스일때 각 사람당 경우의 수
        newO = [] # 모든 사람들의 n개 코스의 경우의 수
        x =sortedOrders(orders)
        for order in x:
            if len(order)<course[i]: continue
            a.append(list(combinations(order,course[i])))  # 각 주문 n개를 먹을때의 경우의수
        for items in a:
            for item in items:
                newO.append(item) # 경우의 수들을 모두 저장
        if(len(newO)==0): break # 만약 coures[i] 개의 주문이 없다면 종료
        countPossible = Counter(newO) # 카운터를 통하여 경우의 수의 개수를 파악
        most = max(countPossible.values()) # 경우의 수의 개수중 가장 큰값
        if(most<2): break # 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 들어가므로 추가하지 않는다
        for key in countPossible.keys():
            if countPossible.get(key) == most:
                answer.append(key) # 만약 최다출현 메뉴라면 answer에 저장한다
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    return sorted(answer)

def sortedOrders (orders):
    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i])) # 주문들을 오름차순으로 정렬
    return orders

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders,course))
