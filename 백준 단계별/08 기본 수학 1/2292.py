N = int(input())

# 1번 방부터 방 한 개로 치므로 초기값 1
roomCnt = 1

address = 1
repeatNum = 1
while N > address:
    address += 6 * repeatNum
    repeatNum += 1
    roomCnt += 1
print(roomCnt)
