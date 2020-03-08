user = input("E  : ")
text = user[11: ]
print(text)
target = text.split(',')[0]
score = text.split(',')[1]
print(target , score)
#/add_score target,3000