num = 12
list_s = []
s = 2
while s <= num: # sがnum以下の間繰り返す
    if num % s == 0: # numがsで割り切れる場合
        num //= s # numをsで割った結果を切り捨て、その値をnumに再代入
        if s not in list_s: # list_sにsがない場合
            list_s.append(s) # sをlist_sに追加
    else:
        s += 1 # list_sにsがある場合、sを1増やす
print(list_s)
