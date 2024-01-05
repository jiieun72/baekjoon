'''
문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
'''

T = int(input())

for i in range(1, T+1):
  A, B = map(int, input().split())

  print("Case #%d : %d + %d = %d" %(i, A, B, A+B))

'''
11021번 문제의 풀이에서 print 부분만 살짝 변형해서

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A , "+" , B , "=" , A+B)

위와 같이 풀이해도 결과는 같다.
그러나, 출력해야하는 변수가 많아졌으므로, 형식지정자를 사용하여 다르게 풀이해보았다.
'''