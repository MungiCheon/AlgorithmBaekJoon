
# 입력
n, k = list(map(int, input("화폐단위갯수, 가치의합 : ").split()))
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

#처리
# cnt = 0
# for coin in coins:
#     if k >= coin:
#         cnt += k // coin
#         k %= coin
#         if k <= 0:
#             break;
# print(cnt)

def solution(K):
    money = K
    cnt = 0
    for coin in coins:
        if money >= coin:
            cnt += (money // coin)
            money %= coin
        else:
            continue
    return cnt

# 출력
print(solution(k))