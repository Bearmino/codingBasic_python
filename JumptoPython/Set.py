# 집합(set)은 파이썬2,3부터 지원하기 시작한 자료형으로, 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
# 집합 자료형은 set 키워드를 사용해 만들 수 있다.
# set()의 괄호 안에 리스트를 입력하거나 문자열을 입력하여 만들 수 있다.
# 비어있는 집합 자료형 set()으로 만들 수 있다.


s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)
# 해당 set을 출력하면 문자가 뒤죽박죽에 문자에 "L"이 하나가 빠져있다. 이는 set의 다음 특징때문이다.
# 1.중복을 허용하지 않는다.
# 2.순서가 없다(Unordered).
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형 값을 얻지만, set은 순서가 없어서 인덱싱 값을 얻을 수 없다.
# 만약, set자료형에 저장된 값을 인덱싱 하기 위해서는 하기에서처럼 리스트나 튜플로 전환해야 한다.

s3 = set([1,2,3])
l1 = list(s3)
print(l1)
print(l1[0])

t1 = tuple(s3)
print(t1)
print(t1[2])

#set을 이용한 교집합, 차집합, 합집합 구하기
# set자료형을 유용하게 사용하는 경우가 교집합, 차집합, 합집합을 구할 때이다.
s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8,9,10])

#교집합(&)
result = s1 & s2
print(result)

#합집합(|)
result = s1 | s2
print(result)

#차집합(-)
result = s1 - s2
result2 = s2 - s1
print(result)
print(result2)

#set과 관련한 함수들
#set에 값 추가(add)
s1 = set([1,2,3])
s1.add(4)
print(s1)

#set에 여러 값 추가(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

#set의 특정값 제거(remove)
s1 = set([1,2,3,4,5])
s1.remove(2)
print(s1)