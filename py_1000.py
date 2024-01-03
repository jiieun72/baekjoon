'''
문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A+B를 출력한다. 
'''

A, B = input().split()
print(int(A)+int(B))

''' 
input() : 사용자로부터 문자열 입력받을 때 사용
          왼쪽에 변수, 오른쪽에 input() 함수 작성하면 입력받은 문자를 변수에 선언할 수 있음
          input 함수로 입력 받는 것은 문자열로 입력 받는 것 --> 사용자가 숫자를 입력하더라도 문자열 형태로 입력 받음
          변수에 직접 숫자를 할당하는 경우 > int , 사용자로부터 숫자를 입력 받는 경우 > string 

********* 입력 함수의 종류 *********
          변수 = input() : 사용자로부터 입력을 받는다.
          변수 = input('문자열') : '문자열'에 해당하는 내용을 출력 후, 사용자로부터 입력을 받는다.

          ex. 
          >>> name = input('What is your name?')
          What is your name? Jieun

================================================================================================================             

split() : 입력받는 문자를 나눌 때 사용하는 함수
          공백으로 구분되어 있는 숫자를 한 줄에 입력받을 경우, 공백을 기준으로 숫자를 나누면 됨
          문자열 뒤에 . 을 붙이고 split()을 써서 사용
          괄호 안에 아무 것도 넣지 않으면, 공백을 기준으로 문자열을 나눔

================================================================================================================   

input().split() : 입력받는 문자가 정해지지 않았으므로, 어떤 문자가 들어오건 공백을 기준으로 나누겠다는 이야기

================================================================================================================   

A, B = input().split() : A, B로 구분한 것은 tuple 자료형의 성질을 이용한 것
                        우측에서 입력받은 문자를 공백을 기준으로 나누게 되면, 두 개의 문자로 나누어지게 됨.
                        그 두 개의 문자를 각각 A, B 변수에 저장하겠다는 의미

================================================================================================================   

print(int(A)+int(B)) : 문자열에서 그냥 + 연산자를 사용하게 되면, 문자 두 개를 연달아 붙여버리는 결과가 나오게 됨 ex. 1+2 >>> 12
                        따라서 입력 받은 두 개의 문자를 숫자(정수형)로 변환하는 과정이 필요 --> int(A), int(B)
                        실수형이면 float(A), float(B)와 같이 강제 형변환

********* 출력 함수의 종류 *********
          print('문자열') : '문자열'을 화면에 출력
          print(변수) : 변수에 해당하는 값을 화면에 출력. 이때 변수값은 모든 변수형이 가능
          print('문자열', 변수) : '문자열'과 변수에 해당하는 값을 연속해서 화면에 출력
'''