numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i]) # 문자열로 만들어 가장 앞의 수를 인덱싱 할 수 있게 한다
    nums =sorted(numbers, key=lambda x:x*3, reverse=True) # 가장 앞에 있는 수를 기준으로 내림차순으로 정렬시킨다
    answer = str(int(''.join(nums)))
    return answer

print(solution(numbers))