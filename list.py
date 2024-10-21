# LIST  = massiv - TIZIM - ARRAY
a = 4
b = [3,54,36,8,43,44,88 ,"dac", false]

# index-pen alu
print(b[0])  # 3

b[2:5]
b[::2]

# index-pen change massiv element
b[2] = 'A'

# appned() = massivke element qosady
b.append('Info')

# remove() = elementti isine  berip joyuga 

b.remove(3)

# pop() = massivtegi elementtin indexsimen joyady
b.pop(5)
# pop() = isi bos bolsa songy indextegi element default-pen joiylady

# clear() = massivti tugel tazartady
b.clear()

# connt() = massiv isinde elementtin  qansa ret kesdesetin sanaidy
b.count(54)

# sort() = osu retimen suruptaidy
b.sort()

# print-pen sygarady sorted()
print(sorted(b))
# al kemu retimnen suryptau .sort(reverse=True)
b.sort(reverse=True)

# reverse() = listti ornalasuyn keri audaryp beredi
b.reverse()

# print-pen mandi list(reversed()) LIST - korsetu kerek
print(list(reversed(b)))

# insert(i,o) = index -pen object salady 
b.insert(2,"43")

# add new array
c= [3,5,7433,77,-54]
print(b+c)
# add new array with mwethod EXTEND()   c array isin ozgertpeidi
b.extend(c)
# sum -summa
sum(c)

# list-ti kobeutu arqyly ulkeutu
print(c*4)

# len
print(len(b))

# max - massivtegi ulken mandi qaitarady
print(max(b))

# min -  massivtegi kisi elementti  qaitarady
print(min(c))

# inndex() = elementtin indexsin qaitarady
b.index(3)

# find element in array with IN bool 
print('JUZ' in b)

# bool  find element array NOT IN 
print('Fald' not in c)







