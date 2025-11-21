list_a = [4,8,3,7,9]
list_b = [10,3,6,7,2]
list_c = [] # 空のリストを作成
i = 0
while i < 5: # iが5未満の間繰り返し
    if  list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
        list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append((list_b[i] - list_a[i]) // 2)
    i += 1 # iをカウント
print(max(list_c)) # 5

'''
i   処理            list_cに追加される値
0   (10 - 4) // 2   3
1   8 - 3 ** 2      -1
2   (6 - 3) // 2    1
3   7 * 2 % 4       2
4   9 - 2 ** 2      5

'''
