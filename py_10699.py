'''
문제 : 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
입력 : 입력은 없다.
출력 : 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
'''

from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d")) 

'''
datetime 패키지를 사용해서 풀이하였다.

아래 링크 참고

https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html
'''