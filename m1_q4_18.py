phrase = 'PythonProgramming'
list_p = [] # 空のリストを作成
for p in phrase: # 繰り返しで位置文字ずつ検査
	if p not in list_p: # pがlist_pにまだ含まれていなければ
		list_p.append(p) # list_pにpを追加
print(len(phrase) - len(list_p)) # 17-11=6つまり重複した文字の数

