#튜플은 리스트와 거의 비슷하지만 다음부분은 리스트와 다르다
# 1) 리스트는 []으로 둘러싸지만, 튜플은 ()으로 둘러싼다.
# 2) 리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 그 값을 바꿀수없다.

#튜플 요솟값을 삭제 시 에러 발생시킴
# t1 = (1,2,'a','b')
# del t1(0)
#
# #튜플 요솟값을 변경 시 에러 발생
# t1= (1,2,'a','b')
# t1[0]='c'
#

#튜플 인덱싱하기
t1 = (1,2,3,4)
print(t1[0])

#튜플 슬라이싱하기
t1 = (1,2,3,4)
print(t1[1:])

#튜플 더하기
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)

#튜플 길이 구하기
t1 = (1,2,3,4,5,6,7,)
print(len(t1))

