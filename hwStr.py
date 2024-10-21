# 1
a =  "ealsda"
print(a)

# 2
print(type(a))

# 3
n = 42
print(a * n)

# 4
print("python\nstr")

# 5
name = input('Enter your name:')
print('Hi, i am ',name)

# 6
num = input(int("enter 15 number"))
num1 = input(int("enter 18 number"))
print(str(num),str(num1))

# 7
word = input("enter any word")
print(word[0] , word[-1])

# 8
word1 = input('enter word with gap')
print(word1.strip())

# 9
wordLove = 'I love python' 
print(wordLove[2:6])


# 10
b = 3293
bStr = str(b)
sum = int(bStr[0]) + int(bStr[1]) + int(bStr[2]) + int(bStr[3])
print(sum)


# 1
str1 = input('Enter any word')
print(str1[0::2])

# 2
print(str1.count('!'))
print(str1.count('?'))
print(str1.count('.'))
print(str1.count(','))

# 3
word2 = "Python nice"
wordRev = word2[0:6]
print(list(reversed(wordRev)))

# 4
year = "EXPO 2016"
yearChange = year.replace('2016' , '2000')
print(year)

# 5
phone = 'Xiaomi Redmi Note 8'
phoneN = phone[-6:-2]
print(phoneN)

# 6
wordF = input('Enter word with F')
print(wordF.find('F'))

# 7
print(word1[0:4] , word[-1:-5])

# 8
print(word.upper())
print(word.strip('r','s'))

# 9
wordA = word1 + wordLove
wordA.isupper()
print(len(wordA))

# 10
anWord = "XYZ!12$hacker$34!ZYX"
print('${}%{}[{}{}}!'.format(anWord[4] , anWord[5],anWord[14] ,anWord[-5]))


