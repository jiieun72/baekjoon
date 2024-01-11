'''
문제 : 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력 : 시험 성적을 출력한다.
'''

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


'''
******* if문 만을 사용한 풀이 *******

score = int(input())

if (90 <= score <= 100) :
  print("A")
if (80 <= score < 90):
  print("B")
if (70 <= score < 80):
  print("C")
if (60 <= score < 70):
  print("D")
if (60 > score):
  print("F")
  
'''