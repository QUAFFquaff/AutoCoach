add_li = [8,7,2,9,4,5,8,7,8,8]
change_li = [0,1,3,5,4,6,7,8,9]
re_li = [0,1,2,3,4,5,5,1,9,5]


line = input()
for i in range(len(line)):
    ind = int(i)
    print(line[i])
    if change_li[ind] >= max(add_li[ind],re_li[ind]):
        print('!')
        print(line[:i]+str(change_li[i])+line[i:])