리스트 = [3, 'hello', 5>3,  True]
튜플=tuple(리스트)


# CRUD - 삭제는 del 연산자
# method : 객체(파이썬을 구성하는 부품)에 소속된 함수
리스트.append(100)      # . < 어디에 소속되어 있는것 / append < method /리스트에 소속 단일사용 불가
리스트[0]=리스트[0]*10
print(리스트)
del 리스트[0]
print(리스트)

