'''
문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/181949

대소문자 바꿔서 출력하기

문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 20
str은 알파벳으로 이루어진 문자열입니다.

입출력 예

입력 #1
aBcDeFg

출력 #1
AbCdEfG
'''

def solution():
    str = input()
    new_str = ''
    for s in str:
        if s.isupper():
            new_str += s.lower()
        else:
            new_str += s.upper()
    print(new_str)

solution()