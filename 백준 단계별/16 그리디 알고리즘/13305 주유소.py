"""
1. 아이디어
현재 위치의 주유소의 리터당 가격보다 싼 주유소까지 거리를 구하고
(그 거리) * (현재 위치 주유소 리터당 가격) 을 구해서 다음 주유소로 넘어가고 더한다.
이걸 반복하다 끝나면 출력한다.

2. 시간복잡도
- O(n^2)

3. 자료구조
N: int;
road: int[];
city: int[];
cost: int;
totalCost: int;
"""
import sys

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

# totalCost = 0
# curCityIdx = 0
# while 1:
#     if curCityIdx == len(city)-1:
#         break
#
#     maxIdx = 0
#     for i in range(curCityIdx+1, len(city)):
#         if city[i] < city[curCityIdx] or i == len(city)-1:
#             maxIdx = i
#             break
#     cost = city[curCityIdx] * sum(road[curCityIdx:maxIdx])
#     totalCost += cost
#
#     curCityIdx = maxIdx
#
# print(totalCost)

curCost = city[0]
totalCost = 0
for i in range(len(city)-1):
    if city[i] < curCost:
        curCost = city[i]
    totalCost += curCost * road[i]

print(totalCost)