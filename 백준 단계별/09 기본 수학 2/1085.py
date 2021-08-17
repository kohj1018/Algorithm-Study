x, y, w, h = map(int, input().split())
distances = [w-x, x, h-y, y]
print(min(distances))
