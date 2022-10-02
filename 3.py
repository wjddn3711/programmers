# 돼지 1 이 0 번째 인덱스 부터 n-2 까지 차례로 선택한다
foods = [3,1,3,1,1,3]
answer = []

poss = [] # 유망한 경우를 저장할 리스트
# 돼지 1 이 0번째 인덱스 부터 n-2 까지 차례로 선택한다
n = len(foods) # 음식의 개수 카운트
for i in range(1, n-2): # 인덱스 슬라이싱을 위해 1 부터 loop
    # 돼지 2, 돼지 3 이 음식을 골고루 가져야 하기 때문에 돼지 1은 최대 n-2 까지 밖에 못먹는다
    pig1 = sum(foods[:i])
    for j in range(1, n-1):
        # 돼지 2 가 돼지 1이 고른 음식의 합계와 같도록 할 수 있는 음식을 고르도록 한다
        if sum(foods[i:i+j]) == pig1:
            # 돼지 2가 음식을 선택한 이후 돼지 3은 j ~ 끝까지의 합
            if sum(foods[i+j:n]) == pig1:
                poss.append([i,j]) # 돼지 1의 선택지점, 돼지 2의 선택지점을 담는다
answer = len(poss)
print(answer)