a = '345'
b = int(a)     #345
c = float(a)   #345.0
d = str(b)     # '345'
# bool은 웬만해서 타입을 바꾸지말자

ar = [3,4,5]
# ar을 튜플로 변환해 br에 저장하시오

br = tuple(ar)

print(type(br))
# 타입을 바꾸려면 바꾸려는 타입의 이름을 사용하면 된다. 

# 리스트에 원소를 추가한다. : append(리스트에서만 사용한다. 리스트에 소속되어있다.)
ar.append(1000)
print(ar)

# .은 멤버연산자라고한다. 
#  어디에 소속되어있다는 의미다.
# 리스트는 전용함수가 있다. 

#append는 프리랜서가 아니라 ar에 소속된 함수 -> method(혼자 다닐수 없다. 단독으로 사용 불가능하다.)
# append는 혼자 사용이 불가능하다. 


# 튜플은 .이 없는게 아니라 append가 없다는 의미다. 



# 메소드는 소속되어 있어서 .을 찍어야 볼 수 있다. list에는 append가 있지만, tuple에는 append가 없다.
# 함수는 이름을 모르면 사용하지 못하지만, 메소드는 이름을 몰라도 대충 찍을 수 있다.

# insert은 리스트에 값을 순서를 정해줄 수 있다. 정렬할 때 많이 사용한다. (정렬은 무조건 오름차순이다.)
ar.insert(2, 45)
print(ar)


# 궁금한거! .은 그럼 메소드를 불러오는 기능인가? list 안에 있는 기능을 불러오는 것 같다.  
# object(객체)와 연관되어 사용된다. -> 사용하고자 하는 대상이 .으로 연결되어있어야함
# 객체란? 어떠한 속성값과 행동을 가지고 있는 데이터입니다.


# 일단 객체와 메소드 그리고 함수에 대해 정확하게 이해를 해야겠다. 
# DB가 정렬해준다. append를 이용해서 값을 그냥 끝에 박아넣고 DB에 전송하면 알아서 정렬해준다.

xr = (10,20,30)
# xr에 40을 추가한 다음 출력하시오.
xr = list(xr)

xr.append(40)
print(xr)

xr = tuple(xr)
print(type(xr))
print(xr)
for item in xr : 
    print(item)

# 마지막은 꼭 원래대로 바꿔줘야한다. 
    

