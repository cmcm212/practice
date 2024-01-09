# 숫자연산 : +, -, *, /,  //(몫), %(나머지)
# 비교연산 : >, >=, <, <=, ==, != -> 결과가 bool(부울)
# 논리연산 : not, and, or -> 입력과 결과가 모두 bool
# 대입연산 : a = 10, a = a + 1, a+=1 
# =, +=, -=, /=, *=........이 대입연산이다.
a = 10 
a *= 5
print(a)

# a += 1, a*=5은 a = a + 1, a= a* 5 이렇게 만들 수 있다.

# 문자에 대해서는 +, * 성립
print('hello' + '시발')

print('hello' * 5)
# 문자에서 *을 사용하면 반복해서 사용된다. 

print("@" * 10)
print("@","@", sep='        ')
print("@","@", sep='        ')
print("@","@", sep='        ')
print("@" * 10)


print("@" * 10)
print("@" ,' '*8,'@', sep='')
print("@" ,' '*8,'@', sep='')
print("@" ,' '*8,'@', sep='')
print("@" * 10)

# ,가 원래 한칸씩 띄우고 한다. 그렇기때문에 *8을 하면 통합 10개가 된다. 
# 여기서 sep을 이용하면 구분자가 sep을 이용해서 결정되서 ,와 상관이 없어진다.  

