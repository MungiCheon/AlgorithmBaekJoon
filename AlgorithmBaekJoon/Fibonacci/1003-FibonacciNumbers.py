N = int(input())
cases = []
for _ in range(N):
    cases.append(int(input())) # 테스트 케이스 입력받기

for case in cases:
    zero_cnt, one_cnt = 1, 0
    for i in range(case):
        zero_cnt, one_cnt = one_cnt, one_cnt + zero_cnt
    print(zero_cnt,one_cnt)