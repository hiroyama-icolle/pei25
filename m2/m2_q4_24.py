def func(a, b):
    if a ** b <= 64: # aのb乗が64以下の場合
        return 1 # 1を返す
    else: # それ以外の場合
        return 0 # 0を返す

x = func(4, 3) # 4の3乗は64なので1となる
y = func(3, 4) # 3の4乗は81なので0となる
z = [bool(x), bool(y)]
print(z) # [True, False]
