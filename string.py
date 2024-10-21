name = "Kaafo"
color = 'red'

print(name+color)

age =32
print('My name is'+" " + name)    
#  " " = konkatiasia
print('My name is', name)  
a = 'salem alem  \n whatsap'
# \n = jana jol

print(a)

# INDEXING
b = "salemJUZ40"
# m - 4 index
b[4]  
b[-2]

# slicing

a[0:8] # salemJUZ
a[2:9] # lemJUZ4

a[5:] # JUZ40

# step
a[0:10:2] # slmU4

# reverse step
a[2: :-1] # las

a[::-1] 
# 04ZUJmelas

# tag element
a[1::2]

# jup elememt
a[0::2]

# string Methods
# 1
soz = 'Informatika'
# count() = ariptin kezdesetin sany
soz.count("t")

soz1 = "almatyl"
# a aribinin qansa ret kesdasetinin sanaidy 3 indexten 10 indexqa deiin

soz1.count("a" , 3 , 11)
# find() ariptin turgan indexsin tauyp beredi
soz1.find('l')

# "l"  aribin 3 ten 11-ga deiingi indexke deiin tauyp beredi
soz1.count("l" , 3 , 11)

# strip() = string-degi aralyqty alyp tastaidy
soz.strip(b)

# replace() = soz aribimen aribin auystyrady
soz.strip('I' , "A")

# isdigit() = sannan turatynyn tekserip jatattyn bool
soz.isdigit()

# isalpha() = aripterden string tolyq boluyn tekseredi
b.isalpha()

# isupper() = ulken aripterden turatunyn tekseretin BOOL

# islower() = kisi arip BOOL

# upper() = ULKEN ARIPKE AUYSTYRADY

# lower() = kisi aripterke change

# split() = string-di list-ke kesip , boledi

# formattau
print("My name is {} I am {} years old".format(name,age))
print(f.'I am  {name} ,I am {age}')

# ord() =  sybmol-dyn ornyn korsetu usin ASCII table qarai tabatyn function

print(ord("A"))

# chr() =  ASCII table- nan  ornyna saikes symboldyn  korsetedi

chr(34) 

# len - length string

print(len(b))


