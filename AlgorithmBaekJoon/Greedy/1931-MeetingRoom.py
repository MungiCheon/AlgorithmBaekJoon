
cnt = 0
pastEnd = 0
N = int(input("회의 갯수 : "))

meet_list = []
for _ in range(N):
    meet_list.append(list(map(int, input().split())))
meet_list.sort(key=lambda x:(x[1], x[0]))

for curStart, curEnd in meet_list:
    if pastEnd <= curStart:
        cnt += 1
        pastEnd = curEnd

print(cnt)

