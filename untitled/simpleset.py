from functools import*      #reduce 함수 사용
def intersect(*ar):     #매개변수에 *이 붙으면 가변인자(튜플로 만들어서 인자 갯수 제한이 없음)
    return reduce(__intersectSC,ar)

def __intersectSC(listX, listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    return reduce(__difference, ar)

def __difference(A,B):
    setList = []
    for x in A:
        if not x in B:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList

A = [1,3,7,10]
B = [2,3,4,9]

print(intersect(A,B))
print(difference(A,B))
print(union(A,B))