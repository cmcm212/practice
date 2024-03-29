jumin = '961011-1021023'

gender = jumin[7]

# 남자인지 여자인지 출력

if gender=='1':
    print('남자')
else:
    print('여자')

# 둘중의 하나 if문을 한줄로 > 삼항연산자
# 복잡한 조건 삼항연산은 쓰지말자 > 스파게티 코드가 됨
print("남자" if gender=='1' else "여자")

# gender가 1또는 3또는 5면 남자, 아니면 여자

print("남자" if gender=='1' or '3' or '5' else "여자")
print("남자" if gender in ('1','3','5') else '여자')

# 주민번호로 나이 출력하기
# 1. 올해의 년도
# 2. 태어난 년도
#   주민번호 앞 2자리를 슬라이싱한다 -> year
#    주민번호 7번째 자리가 '1','2' -> '19'+year
#    주민번호 7번째 자리가 '3','4' -> '20'+year
# 3. 올해의 년도 - int(태어난 년도)

import datetime
this_year = datetime.datetime.now().year
year = jumin[0:2]
if jumin[7] in ('1', '2'):
    year = int('19' + year)
elif jumin[7] in ('3', '4'):
    year = int('20' + year)
else:
    print('잘못된 입력')
print(f'{this_year-year}세')