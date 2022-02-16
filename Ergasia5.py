
#Topotheteiste to file sto open
file  = open("C:/Users/stefan/Desktop/Python/t.txt", "r")
file_content = file.read()
range1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
w = ""
for char in file_content:
    if char in range1:
        w = w + char
    else:
        w = w + " "

w = w.lower()  
w = w.split(" ") 
x = 0
while True:
    if x == len(w):
        break
    if w[x] == "":
        w.pop(x)
    else:
        x += 1

uniword = []
counter = []
tempArray = []

for x in w:
    if not x in uniword:
        uniword.append(x)
        counter.append(1)
    else:
        counter[uniword.index(x)] += 1

y = 0
while y < 10:
    maxCounter = max(counter)
    print(max(counter))
    maxIndex = counter.index(maxCounter)
    print(uniword[maxIndex])
    tempArray.append(uniword[maxIndex])
    counter.pop(maxIndex)
    uniword.pop(maxIndex)
    y += 1

z = 0
while z < 10:
    uniword.append(tempArray[0])
    tempArray.pop(0)
    z += 1

#kathe lexi 8a metri8ei mia fora gia to sundiasmo twn grammatwn

i = input("Ari8mos sundiasmos grammatwon (2/3)")
if i == "2" :
    a = 0
    let2 = []
    while a < len(uniword):
        let2.append(uniword[0][:2])
        uniword.pop(0)
        a += 1

    x2 = 0
    uniword2 = []
    count2 = []
    for x2 in let2:
        if not x2 in uniword2:
            uniword2.append(x2)
            count2.append(1)
        else:
            count2[uniword2.index(x2)] += 1

    y2 = 0
    while y2 < 10:
        maxCounter2 = max(count2)
        print(max(count2))
        maxIndex2 = count2.index(maxCounter2)
        print(uniword2[maxIndex2])
        count2.pop(maxIndex2)
        uniword2.pop(maxIndex2)
        y2 += 1
   

if i == "3":
    a = 0
    let2 = []
    while a < len(uniword):
        let2.append(uniword[0][:3])
        uniword.pop(0)
        a += 1

    x2 = 0
    uniword2 = []
    count2 = []
    for x2 in let2:
        if not x2 in uniword2:
            uniword2.append(x2)
            count2.append(1)
        else:
            count2[uniword2.index(x2)] += 1

    y2 = 0
    while y2 < 10:
        maxCounter2 = max(count2)
        print(max(count2))
        maxIndex2 = count2.index(maxCounter2)
        print(uniword2[maxIndex2])
        count2.pop(maxIndex2)
        uniword2.pop(maxIndex2)
        y2 += 1


        

input()