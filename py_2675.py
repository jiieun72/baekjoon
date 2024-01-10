'''
문제 : 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
       즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
       QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
입력 : 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
       S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
출력 : 각 테스트 케이스에 대해 P를 출력한다. 
'''

t = int(input())

for i in range(t):
       R, S = input().split()
       R, S = int(R), str(S)

       for i in range(len(S)):
              print(R*S[i], end='')
       print()

'''
테스트 케이스 개수는 첫 번째 줄 변수 t로 설정하여 int 형으로 받고, 이 테스트 케이스의 개수만큼 반복되어야하므로 이 값을 for 문에 집어넣어 반복문을 작성한다.
R, S는 각각 공백으로 구분되는 정수형, 문자열의 형식이므로 int, str 형으로 강제 형변환을 시켜준다.

이후, 문자열을 R(반복 횟수)만큼 반복하여 출력해주는 for문을 작성해주면 된다.

이때, end='' 를 작성해주지 않으면 결과가 한 줄에 출력되는 것이 아니라 줄이 바뀌어서 출력된다.

... print(R*S[i]) ...
ex. 
1
3 abc
aaa
bbb
ccc

문제의 예제 출력에서는 문자를 한 줄에 출력했으므로 print(R*S[i], end='') 로 작성해주어야 한다.
'''