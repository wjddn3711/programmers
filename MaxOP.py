"""
1. 연산자는 +, - , * 세가지 종류이다
2. 연산자의 우선순위는 명시적으로 알 수 없으며 그리디하게 각 우선순위 별로 값을 구하여 그중 최대값을 구해야한다
3. 최종적으로 연산되어 지는 값은 절대값을 통하여 비교를 진행한다
"""
from itertools import permutations

expression = "100-200*300-500+20"
def solution(expression):
    # 우선 연산자의 우선순위를 무작위로 알아낸다
    answer = []
    operator = ['*','-','+']
    prob = list(permutations(operator,3))
    for op in prob:
        # 우선순위가 주어졌을 때 우선순위에 맞게 계산하는 함수
        # 최종적으로 계산된 값이 출력된다
        answer.append(abs(int(calOp(op,expression,0))))
    return max(answer)


def calOp(op,exp,index):
    if exp.isdigit():
        #만약 수식이 없는 숫자만으로 이루어져 있다면
        return str(exp)
    else:
        if op[index]=='*':
            splitted = exp.split('*') # 해당 연산자를 기준으로 나눠준다
            temp = [] # 임시적으로 스플릿한 것들을 담을 리스트
            for s in splitted:
                temp.append(calOp(op,s,index+1)) # 다음 연산자를 통하여 쪼개진 식을 다시 계산한다
            return str(eval('*'.join(temp))) # 모두 수식으로 이루어져 있을 때, temp 에는 수식만 있고 이를 * 조인하여 계산하여 반환한다
        elif op[index]=='-':
            splitted = exp.split('-') # 해당 연산자를 기준으로 나눠준다
            temp = [] # 임시적으로 스플릿한 것들을 담을 리스트
            for s in splitted:
                temp.append(calOp(op,s,index+1)) # 다음 연산자를 통하여 쪼개진 식을 다시 계산한다
            return str(eval('-'.join(temp)))
        else: # + 연산자인 경우
            splitted = exp.split('+') # 해당 연산자를 기준으로 나눠준다
            temp = [] # 임시적으로 스플릿한 것들을 담을 리스트
            for s in splitted:
                temp.append(calOp(op,s,index+1)) # 다음 연산자를 통하여 쪼개진 식을 다시 계산한다
            return str(eval('+'.join(temp)))

solution(expression)