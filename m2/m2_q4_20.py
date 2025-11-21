num = 3
list_a = [] # 空のリストを作成
while num < 5: # numが5未満の時繰り返す
    for i in range(num, 10, 3): # num=3の場合、3から10まで3つおき、つまり[3, 6, 9]
        i -= 6 # i-6をiに代入
        list_a.append(i) # list_aにiを追加
    num += 1 # numを1増やす
print(sum(list_a)) # 合計を出力

'''
num         3           4
i           3, 6, 9     4, 7
list_a      -3, 0, 3    -2, 1

''' 
