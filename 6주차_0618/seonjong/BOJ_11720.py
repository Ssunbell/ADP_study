# 문제 링크 : https://www.acmicpc.net/problem/11720

answer = 0
N = int(input())
splited_num = map(int, list(input()))
for number in splited_num:
    answer += number

print(answer)

answer = 0
N = int(input())
num = input()
for i in range(N):
    answer += int(num[i])
    
print(answer)