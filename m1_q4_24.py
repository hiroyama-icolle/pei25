animals = ['Dog','Cat','Rabbit','Horse','Dorlphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D') #animalが'D'で始まる場合True、そうでない場合Falseを返す
    is_long = len(animal) > 5 # animalの文字数が6文字以上ならTrue
    if from_D and is_long:
        break # どちらもTrueならbreak
    elif not from_D and is_long:
        total += animal.find('b') # 最初に'b'が現れるインデックスを返し、見つからなければ-1を返す
    else:
        total += len(animal)
print(total)
