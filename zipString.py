def solution(s):
    answer = []
    if len(s)==1: # 문자열의 길이가 1 밖에 안된다면 1을 바로 반환한다
        return 1
    for c in range(1,(len(s)//2)+1): # 중복되는 문자열은 최대 해당하는 문자열의 절반까지임을 감안한다
        cut = s[:c]
        count = 1
        result = ""
        for char in range(c,len(s),c): # c 의 길이만큼 슬라이싱하여 해당하는 cut 이 중복되는 경우 count를 1 늘려준다
            if cut == s[char:char+c]:
                count+=1
            else:
                if count == 1:
                    count = str("") # 만약 count 가 1이라면 생략
                result += str(count)+cut # 결과에 정보 추가
                cut = s[char:char+c] # 새로운 문자열이 기준이 되어 압축을 진행
                count = 1 # 카운트를 다시 0으로 초기화
        if count == 1:
            count = str("")
        result += str(count) + cut # 마지막 나머지 반을 저장하기위해
        answer.append(len(result))
    return min(answer)

s = "ababcdcdababcdcd"
answer = []
for c in range(1,(len(s)//2)+1): # 중복되는 문자열은 최대 해당하는 문자열의 절반까지임을 감안한다
    cut = s[:c]
    count = 1
    result = ""
    for char in range(c,len(s),c): # c 의 길이만큼 슬라이싱하여 해당하는 cut 이 중복되는 경우 count를 1 늘려준다
        if cut == s[char:char+c]:
            count+=1
        else:
            if count == 1:
                count = str("") # 만약 count 가 1이라면 생략
            result += str(count)+cut # 결과에 정보 추가
            cut = s[char:char+c] # 새로운 문자열이 기준이 되어 압축을 진행
            count = 1 # 카운트를 다시 0으로 초기화
    if count == 1:
        count = str("")
    result += str(count) + cut # 마지막 나머지 반을 저장하기위해
    answer.append(result)

print(answer)