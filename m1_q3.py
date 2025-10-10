a = 12
b = 5
print(b - a) # (12)
print(b - abs(2 * b - a) * 3) # (13)
print("{0:05b}".format(b)) # (14)
c = [2, 7, 15, 12, 9]
c.sort()
print(c) # (15)
print(c[2:3]) # (16) インデックス2から3の手前までのスライスをリストで返す
print(f'{(a - b) / c[3]:->8.3f}') # (17)

