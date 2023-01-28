'''
print("19/3의 결과\n몫:",19//3,"\n나머지:",19%3)

num=10
num+=14
print(num)

num1=int(input( "first: "))
num2=int(input("second:"))
print(num2-num1, num1*num2)

num1=int(input("f:"))
num2=int(input("s:"))
num3=int(input("t:"))
print(num1*num2+num3)

num=int(input("z:"))
print(pow(num,2))

num1=int(input("f:"))
num2=int(input("s:"))
print("30>20:",num1>num2,"\n30<20:",num1<num2)

num=int(input("n"))
print(-num)

num1=int(input("a"))
num2=int(input("b"))
if num1>num2:
    print(num1,"과",num2,"중 큰수는",num1,"이며 두 수의 차는",num1-num2)
elif num1<num2:
        print(num1,"과",num2,"중 큰수는",num2,"이며 두 수의 차는",num2-num1)
else :
    print(num1,"과", num2,"는 같은 수이며 두 수의 차는", 0," 이다")

n=int(input("a"))
if n>0:
    print("양수")
elif n<0:
        print("음수")
else :
            print("0")

s=(input("s"))
a=int(input("age"))
if s=="남자":
    print("남자")
    if a <=19:
        print("미성년자")
    elif a<=59:
        print("성인")
    else:
        print("노인")
else:
    print("여자", a//10*10,"대")
'''

print("Hello world")
