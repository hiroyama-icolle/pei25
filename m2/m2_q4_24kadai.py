def func(a, b):
    if a ** b <= 64: # aのb乗が64以下の場合
        return 1 # 1を返す
    else: # それ以外の場合
        return 0 # 0を返す

x = func(4, 3) # 4の3乗は64なので1となる
y = func(3, 4) # 3の4乗は81なので0となる
a = func(5, 6) # 5の6乗は大きい数

z = [bool(x), bool(y), bool(a)]
print(z) # [True, False]

'''
複数行のコメントはクォーテーション３つで囲う
bool()関数についてまとめましょう
TrueかFalseが返される

'''
