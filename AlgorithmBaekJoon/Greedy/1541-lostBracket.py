
N = input().split('-') # A-B+C 식일 경우 [A,B+C] 배열 생성
nums = []

for a in N:
    sum = 0
    tmp = a.split('+') # [[A] , [B+C]] 구성의 배열 생성
    for b in tmp:
        sum += int(b) # 덧셈부터 실행
    nums.append(sum) # 계산 완료된 값들을 저장
result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i] # 계산 완료된 값들을 대상으로 뺄셈 실행
print(result)