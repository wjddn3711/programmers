from collections import Counter
def solution(str1, str2):
    answer = 0
    a,b =sets(str1,str2) # str1 집합을 a 로, str2는 b로 지정
    cA = Counter(a)
    cB = Counter(b)
    intersec = list((cA&cB).elements())
    union = list((cA|cB).elements())
    if len(intersec)==0 and len(union)==0: return 65536
    answer = int(len(intersec) / len(union) * 65536)
    return answer

def sets(str1, str2):
    A = []
    B = []
    # 두개씩 슬라이스하여 저장한다
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2])
    return A,B

str1 = "aa1+aa2"
str2 = "AAAA12"

solution(str1,str2)
