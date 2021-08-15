A, B, C = [int(i) for i in input().split()]
print( (A+B)%C )
print( ((A%C) + (B%C))%C )
print( (A*B)%C )
print( ((A%C) * (B%C))%C )