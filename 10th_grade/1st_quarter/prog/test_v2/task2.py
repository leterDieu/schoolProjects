import math
import json

logs_list = [math.ceil(math.log(i, 3)) for i in range(1, 2000010)]
sums_list = [0]
for elem in logs_list:
    sums_list.append(sums_list[-1] + elem)


def func(start: str, end: str) -> int:
    start, end = int(start), int(end)

    return 2 * logs_list[start] + sums_list[end + 1] - sums_list[start + 1]


for _ in range(int(input())):
    print(func(*input().split()))
