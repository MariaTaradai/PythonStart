dict_one = {}
l = [ 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd' ]
for i in l :
    count = dict_one.get(i)
    if count:
        dict_one[i] = count + 1
    else :
        dict_one[i] = 1
print(dict_one)        
