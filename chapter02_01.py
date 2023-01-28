#chaapter2-1
#print 사용법

 #기본 출력
 #''문자, ""문자열, ''' '''랑""" """는 여러줄=\n으로도 가능
 # 'python's blah'의 경우 'python\'s blah' 해주면 됨=escape  
'''
print("python start!")
print('python')
print(''' ''')
print("""python2""")
print()

#separator  option
print('p','y', sep='_')
print('010','1234','5678', sep='-')
print("pyth","google.com", sep='@')
print()

#end option
print("welcome to", end=' ')
print("IT News", end='+')
print("web site")
print()

#file option
import sys
print("Learn python", file=sys.stdout)
print()

#format 사용(d_정수_3,s_문자열_"python",f_실수_3.141592)
print('%s %s' % ('one', 'two')) #문자열 배정해줌
print('{}{}'.format('one', 'two')) #문자열이든 아니든 포맷에 맞춰 배정
print('{1}{0}'.format('one','two')) #{}안의 숫자는 입력될 순서, 없을 시 임으로 배정
print()

# %s
print('%10s' % ("nice")) #%10s는 열자리를 채우는데 공백을 왼쪽부터 채워
print('{:>10}'.format("nice")) #{:>10s}는 열자리를 채우는데 공백을 왼쪽부터 채워

print('%-10s' % ("nice")) #%-10s는 열자리를 채우는데 공백을 오른쪽부터 채워(한마디로 숫자가 양수면 왼쪽,음수면 오른쪽부터 채움)
print('{:10}'.format("nice")) #{:10}는 열자리를 채우는데 공백을 오른쪽부터 채워

print('{:_>10}'.format("nice")) #공백을 _로 채워
print('{:^10}'.format("nice")) #중앙정렬

print('%.5s' % ("nice"))
print('%.5s' % ("pythonstudy")) #%.5s는 다섯자리까지 절삭한다는 뜻, .이 없으면 5자리 확보+글자수 넘어가도 그냥 다 들어옴, .이 있어야 절삭(공백X)
print('{:10.5}'.format("pythonstudy")) #10자리를 확보하는데 5자리까지 절삭(한마디로 5자리 이후 공백O)

# %d_정수
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(453)) #문자열일땐 s를 붙여줄 필요없었지만 정수일땐 d를 붙여줘야함

# %f_실수
print('%f'% (3.1415929597))
print('{:f}'.format (3.1415929597))

print('%6.3f' % (3.1415929597)) #6은 전체 자릿수를 의미(.포함), 3은 소수점 자리
print('{:6.3f}'.format(3.1415929597))
'''