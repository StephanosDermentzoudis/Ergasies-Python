
#Topotheteiste to file sto open
file  = open("C:/Users/stefan/Desktop/Python/t.txt", "r")
file_content = file.read()
range1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
w = ""
for char in file_content:
    if char in range1:
        w = w + char
    else:
        w = w + " "
  
w = w.split(" ") 
x = 0
while True:
    if x == len(w):
        break
    if w[x] == "":
        w.pop(x)
    else:
        x += 1

words = []
words = w

print(len(words) , "words in total")
len1 = []
len2 = []
len3 = []
len4 = []
len5 = []
len6 = []
len7 = []
len8 = []
len9 = []
len10 = []
len11 = []
len12 = []
len13 = []
len14 = []
len15 = []
len16 = []
len17 = []
len18 = []
len19 = []

while len(words) > 0:
    if len(words[0]) == 1:
        len1.append(words[0])
        words.pop(0)
    elif len(words[0]) == 2:
        len2.append(words[0])
        words.pop(0)  
    elif len(words[0]) == 3:
        len3.append(words[0])
        words.pop(0)
    elif len(words[0]) == 4:
        len4.append(words[0])
        words.pop(0)
    elif len(words[0]) == 5:
        len5.append(words[0])
        words.pop(0)
    elif len(words[0]) == 6:
        len6.append(words[0])
        words.pop(0)
    elif len(words[0]) == 7:
        len7.append(words[0])
        words.pop(0)
    elif len(words[0]) == 8:
        len8.append(words[0])
        words.pop(0)
    elif len(words[0]) == 9:
        len9.append(words[0])
        words.pop(0)
    elif len(words[0]) == 10:
        len10.append(words[0])
        words.pop(0)
    elif len(words[0]) == 11:
        len11.append(words[0])
        words.pop(0)
    elif len(words[0]) == 12:
        len12.append(words[0])
        words.pop(0)
    elif len(words[0]) == 13:
        len13.append(words[0])
        words.pop(0)
    elif len(words[0]) == 14:
        len14.append(words[0])
        words.pop(0)
    elif len(words[0]) == 15:
        len15.append(words[0])
        words.pop(0)
    elif len(words[0]) == 16:
        len16.append(words[0])
        words.pop(0)
    elif len(words[0]) == 17:
        len17.append(words[0])
        words.pop(0)
    elif len(words[0]) == 18:
        len18.append(words[0])
        words.pop(0)
    elif len(words[0]) == 19:
        len19.append(words[0])
        words.pop(0)
    

print(len(len1) , "word(s) with 1 letter")
print(len(len2) , "word(s) with 2 letters")
print(len(len3) , "word(s) with 3 letters")
print(len(len4) , "word(s) with 4 letters")
print(len(len5) , "word(s) with 5 letters")
print(len(len6) , "word(s) with 6 letters")
print(len(len7) , "word(s) with 7 letters")
print(len(len8) , "word(s) with 8 letters")
print(len(len9) , "word(s) with 9 letters")
print(len(len10) , "word(s) with 10 letters")
print(len(len11) , "word(s) with 11 letters")
print(len(len12) , "word(s) with 12 letters")
print(len(len13) , "word(s) with 13 letters")
print(len(len14) , "word(s) with 14 letters")
print(len(len15) , "word(s) with 15 letters")
print(len(len16) , "word(s) with 16 letters")
print(len(len17) , "word(s) with 17 letters")
print(len(len18) , "word(s) with 18 letters")
print(len(len19) , "word(s) with 19 letters")

pair1 = len(len1) - len(len19)
if pair1 > 0:
    print(abs(pair1) , "word(s) with 1 letter remaining")
else:
    print(abs(pair1) ,"word(s) with 19 letters remaining")

pair2 = len(len2) - len(len18)
if pair2 > 0:
    print(abs(pair2) , "word(s) with 2 letters remaining")
else:
    print(abs(pair2) ,"word(s) with 18 letters remaining")

pair3 = len(len3) - len(len17)
if pair3 > 0:
    print(abs(pair3) , "word(s) with 3 letters remaining")
else:
    print(abs(pair3) ,"word(s) with 17 letters remaining")

pair4 = len(len4) - len(len16)
if pair4 > 0:
    print(abs(pair4) , "word(s) with 4 letters remaining")
else:
    print(abs(pair4) ,"word(s) with 16 letters remaining")

pair5 = len(len5) - len(len15)
if pair5 > 0:
    print(abs(pair5) , "word(s) with 5 letters remaining")
else:
    print(abs(pair5) ,"word(s) with 15 letters remaining")

pair6 = len(len6) - len(len14)
if pair6 > 0:
    print(abs(pair6) , "word(s) with 6 letters remaining")
else:
    print(abs(pair6) ,"word(s) with 14 letters remaining")

pair7 = len(len7) - len(len13)
if pair7 > 0:
    print(abs(pair7) , "word(s) with 7 letters remaining")
else:
    print(abs(pair7) ,"word(s) with 13 letters remaining")

pair8 = len(len8) - len(len12)
if pair8 > 0:
    print(abs(pair8) , "word(s) with 8 letters remaining")
else:
    print(abs(pair8) ,"word(s) with 12 letters remaining")

pair9 = len(len9) - len(len11)
if pair9 > 0:
    print(abs(pair9) , "word(s) with 9 letters remaining")
else:
    print(abs(pair9) ,"word(s) with 11 letters remaining")

pair10 = len(len10) / 2
if len(len10)%2 == 0:
    print("0 words with 10 letters remaining")
else:
    print("1 word with 10 letters remaining")





input() 