#정규표현식(regular expressions)
# 복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬뿐 아니라 C, 자바, 심지어 문서 작성 프로그램 등 문자열을 처리해야 하는 다양한 곳에서 활용
# 정규식 사용시에는 re모듈을 사용한다..

# 예제)
# 다음과 같이 주민 등록 번호가 포함한 텍스트를 블로그에 올리려 한다.
#
# 홍길동의 주민번호는 800905-1049118 입니다.
# 그리고 고길동의 주민번호는 700905-1059119 입니다.
# 그렇다면 누가 형님일까요?
# 그러나 개인정보를 그대로 올릴 수는 없으므로 주민 등록 번호 뒷자리는 모두 * 문자로 마스킹하고자 한다.
# 어떻게 프로그램을 작성해야 정해진 형식의 문자열을 간단하게 바꿀 수 있을까?

# 기본방식)
data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 1. 공백 문자를 기준으로 전체 텍스트를 나눈다(split() 함수 사용).
# 2. 나눈 단어가 주민 등록 번호 형식인지 조사한다.
# 3. 주민 등록 번호 형식이라면 뒷자리를 *******로 마스킹한다.
# 4. 나눈 단어를 다시 조립한다.

# 정규식을 사용

import re

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******",data))

# re.compile("(\d{6})[-]\d{7}")에서 사용한 (\d{6})[-]\d{7}과 같은 문자열을 정규표현식이다.
# 숫자6 + 붙임표(-) + 숫자7 (단, 숫자6은 괄호를 사용하여 그룹으로 지정했다.)
# 즉, 주민 등록 번호와 일치하는 정규표현식이다. 이 정규표현식을 이용하여 re.compile() 함수로 만든 객체에 sub() 함수를 사용하면
# 이 식과 일치하는 문자열 일부분을 *로 바꿀 수 있다.
#
# pat.sub("\g<1>-*******", data) 코드가 바로 data 문자열에서 주민 등록 번호 형식 문자열을 찾아 주민 등록 번호의 뒷부분만
# *******로 바꾸는 역할을 한다. 여기서 \g<1>은 정규표현식과 일치하는 문자열 중 첫 번째 그룹을 의미한다.
# 정규표현식에서 그룹을 지정하려면 (\d{6})처럼 괄호로 묶으면 되는데, 여기서 첫 번째 그룹 \g<1>은 주민 등록 번호 형식 문자열에서
# 바꾸지 않고 그대로 사용할 주민 등록 번호 앞부분을 뜻한다.

# 출력)
# 홍길동의 주민번호는 800905-******* 입니다.
# 그리고 고길동의 주민번호는 700905-******* 입니다.
# 그렇다면 누가 형님일까요?

# 두 코드의 출력값은 같지만, 정규식을 이용하면 한결 간결해진다.

