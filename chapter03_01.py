# 숫자형

# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린(참/거짓)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입
str1 = "python"
bool= True
str2 = 'Anaconda'
float2 = 10.0 # 10 == 10.0 아님, 정수타입과 플롯타입이니까
int2 = 7
list = [str1, str2] #데이터 적재가능
dict = {
    "name": "Machine Learning", #name, version은 키, 사전이라고 보면 됨
    "Version": 2.0
}
tuple = (7,8,9) #괄호없이 ,로만 이어도 튜플로 인식
set = {7,8,9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float2))
print(type(int2))
print(type(dict))

# 숫자형 연산자
'''
+ - * /
// : 몫만 산출
% : 나머지만 산출
abs(x) : 절대값
pow(x,y) : x의 y제곱? == x**y -> x=2, y=3 2의 세제곱
'''

# 형 변환
a = 3.
b = 6
c = .7
d = 12.7

#형 변환
print(float(b))
print(int(c)) #정수를 플롯에 넣으면 실수로, 실수를 인트에 넣으면 정수로 치환됨
print(int(True)) # True : 1, False : 0 을 의미
print(float(False)) # 실수에 넣으면 0.0으로
print(complex(3))
print(complex('3')) #문자형 -> 숫자형으로 자동 치환되서 출력]
