# 1. 하기의 영화 예매순서를 move_rank이름의 리스트에 저장해보자.(순위는 중요하지 않다.)
# [1위 닥터 스트레인지]
# [2위 스플릿]
# [3위 해리포터]
move_rank = ["닥터 스트레인지","스플릿","해리포터"]
print(move_rank)

# 2. 영화 예매순서 리스트에 "배트맨"을 추가해보자.
move_rank.append("배트맨")
print(move_rank)

# 3. 영화 예매순서에서 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿"상에 추가해보자.
move_rank.insert(1,"슈퍼맨")
print(move_rank)

# 4. 영화 예매순서에서 "해리포터"를 삭제해보자.
move_rank.remove("해리포터")
print(move_rank)

# 5. 영화 예매순서에서 "스플릿"과 "배트맨"을 삭제해보자.
del move_rank[2]
del move_rank[2]
print(move_rank)

# 6. 두 리스트의 값을 모두 가지는 하나의 리스트 langs로 통합해보자.
lang1=["C","C++","Java"]
lang2=["Python","Go","C#"]
langs = lang1+lang2
print(langs)

# 7. 다음 리스트에서 최대값과 최소값을 구해보세요.
numbers = [1,2,3,4,5,6,7,8,9,10]
print(max(numbers))
print(min(numbers))

# 8. 다음 리스트의 합을 구해보세요.
numbers = [1,2,3,4,5,6,7]
print(sum(numbers))

# 9. 다음 리스트에 저장된 데이터의 개수를 화면에 구해보자.
cook = ["피자","김밥","튀김","만두","족발","라면"]
print(len(cook))

# 10. 다음 리스트의 평균을 구해보자.
numbers = [1,2,3,4,5]
print(sum(numbers)/len(numbers))

# 11. 하기의 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하자.
price = ['20180728',100,130,140,150,160,170]
print(price[1:])

# 12. 하기의 nums 변수에서 슬라이싱을 통해서 홀수만 출력해보자.
nums = [1,2,3,4,5,6,7,8,10]
print(nums[::2])
print(nums[1::2])

# 13. 슬라이싱을 사용해서 리스트의 숫자를 역방향으로 출력해보자.
nums = [1,2,3,4,5]
print(nums[::-1])

# 14. 하기의 interest 변수에 있는 리스트 자료에서 "삼성전자", "naver"만 나오게 출력해보자.
interest = ['삼성전자','현대','google','naver']
print(interest[0],interest[3])

# 15.