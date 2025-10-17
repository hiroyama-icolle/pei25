a = 17
b = 5
dm = divmod(a, b) # 商と余りをタプルで返す
p = pow(dm[0], dm[1]) # 3**2 = 9を返す
all_num = [a, b, dm[0], dm[1], p] #[17, 5, 3, 2, 9]
min_all = min(all_num) # 最小値2を代入
max_all = max(all_num) # 最大値17を代入
sum_all = sum(all_num) # 合計値36を代入
print(f'{min_all}, {max_all}, {sum_all}') #f文字列
print(all_num) # 課題


