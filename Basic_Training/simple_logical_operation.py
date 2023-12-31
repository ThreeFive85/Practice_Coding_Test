'''
문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/181917

간단한 논리 연산

문제 설명
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

(x1 v x2) ^ (x3 v x4)
입출력 예
x1	    x2	    x3	    x4	    result
false	true	true	true	true
true	false	false	false	false

입출력 예 설명
입출력 예 #1

예제 1번의 x1, x2, x3, x4로 식을 계산하면 다음과 같습니다.

(x1 v x2) ^ (x3 v x4) ≡ (F v T) ^ (T v T) ≡ T ^ T ≡ T

따라서 true를 return 합니다.

입출력 예 #2

예제 2번의 x1, x2, x3, x4로 식을 계산하면 다음과 같습니다.

(x1 v x2) ^ (x3 v x4) ≡ (T v F) ^ (F v F) ≡ T ^ F ≡ F

따라서 false를 return 합니다.

v과 ^의 진리표는 다음과 같습니다.

x	y	x v y	x ^ y
T	T	  T	      T
T	F	  T	      F
F	T	  T	      F
F	F	  F	      F
'''
def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer