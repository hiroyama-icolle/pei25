animals = ['Dog','Cat','Rabbit','Horse','Dorlphin']
total = 0
for animal in animals:
    print(f'totalの数は{total}') # 課題
    from_D = animal.startswith('D') #animalが'D'で始まる場合True、そうでない場合Falseを返す
    is_long = len(animal) > 5 # animalの文字数が6文字以上ならTrue
    if from_D and is_long:
        break # どちらもTrueならbreak
    elif not from_D and is_long:
        total += animal.find('b') # 最初に'b'が現れるインデックスを返し、見つからなければ-1を返す
    else:
        total += len(animal)
print(total)

'''
繰り返しの中でtotalの値はどのように変化しているか観察したいです
そのためのprint(total)関数をどこに挿入したら良いでしょう？

【実行例】
totalの値は0
totalの値は3
totalの値は6
totalの値は8
totalの値は13
13

'''
