'''
문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A+B를 출력한다.
'''

A = int(input())
B = int(input())

print(A+B)

'''
A+B의 값을 한 줄에 출력해야한다는 점은 1000번 문제와 동일하지만,
이번 문제는 A, B의 값을 각각 한 줄에 입력 받아야했으므로 input() 함수를 각 변수에 사용하여 풀이하였다.

    A = input()
    B = input()
    print(int(A)+int(B))

    A, B = int(input()), int(input())
    print(A+B)

등등 다양한 방식으로 풀이할 수 있다.
'''