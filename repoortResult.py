from collections import Counter


def solution(id_list, report, k):
    answer = []
    nameList = dict()
    for r in report:
        names = r.split()
        if names[0] not in nameList.keys():
            nameList[names[0]] = [names[1]]
        else: # 만약 해당하는 아이디의 신고내역이 존재한다면 기존에 있던 딕셔너리에 추가한다
            if(names[1] not in nameList.get(names[0])): # 동일한 이름을 신고한 이력이 없다면
                nameList.get(names[0]).append(names[1])

    reportList = []
    for id in id_list:
        cnt = 0
        for nl in list(nameList.values()):
            if id in nl:
                cnt += 1
        if cnt>=k :
            reportList.append(id)

    for id in id_list:
        cnt = 0
        if id in nameList.keys(): # 만약 신고한 이력이 있다면
            for reported in reportList:
                if reported in nameList.get(id):
                    cnt+=1
        answer.append(cnt)
    return answer


# k = 3
#
#
# nameList = dict()
# for r in report:
#     names = r.split()
#     if names[0] not in nameList.keys():
#         nameList[names[0]] = [names[1]]
#     else: # 만약 해당하는 아이디의 신고내역이 존재한다면 기존에 있던 딕셔너리에 추가한다
#         if(names[1] not in nameList.get(names[0])): # 동일한 이름을 신고한 이력이 없다면
#             nameList.get(names[0]).append(names[1])
#
# for key in nameList.keys():
#     print(key, " = ",nameList.get(key))
#
# reportList = []
# for id in id_list:
#     cnt = 0
#     for nl in list(nameList.values()):
#         if id in nl:
#            cnt += nl.count(id)
#     if cnt>=k :
#         reportList.append(id)
#
# answer = []
# for id in id_list:
#     cnt = 0
#     if id in nameList.keys(): # 만약 신고한 이력이 있다면
#         for reported in reportList:
#             if reported in nameList.get(id):
#                 cnt+=1
#     answer.append(cnt)
#
# print(answer)