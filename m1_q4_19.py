a = [1, 2, 3, 4]
id_a = id(a) # aのIDをid_aに代入
b = a.copy() # aのコピーをbに代入(別のオブジェクト)
id_b = id(b) # bが指すオブジェクトID（識別子）をid_bに代入
if id_a == id_b:
    result = 'A' # aとbが同じオブジェクトの場合
elif id(a) == id(b):
    result = 'B' # aとbの現在のIDが同じ場合
elif id_a == id(a):
    result = 'C' # id_aがaのIDと等しい場合
else:
    result = 'D'
print(result) # 答えはC

