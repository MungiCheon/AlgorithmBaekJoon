
n = int(input("인원수를 입력하세요: "))
min_list = list(map(int, input("시간을 입력하세요: ").split()))

def greedy(N, P):
    result = 0
    # 오름차순
    P.sort(reverse=False)
    for min in range(1, N+1):
        result += sum(min_list[0:min])

    return result

print(greedy(n, min_list))