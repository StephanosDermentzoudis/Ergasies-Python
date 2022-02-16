#Topotheteiste to file sto open
file  = open("C:/Users/stefan/Desktop/Python/t.txt", "r")
file_content = file.read()
bitestemp = ' '.join(format(ord(x), 'b') for x in file_content)
lent = len(bitestemp)
bites = []
a1 = ""
b1 = ""
a2 = ""
b2 = ""
a3 = ""
b3 = ""
a4 = ""
b4 = ""
x = ""
i = 0
while i < int(lent):
    a1 = bitestemp[i: i + 2]
    b1 = bitestemp[i + 5:i + 7]
    a2 = bitestemp[i + 8: i + 10]
    b2 = bitestemp[i + 13:i + 15]
    a3 = bitestemp[i + 16: i + 18]
    b3 = bitestemp[i + 21:i + 23]
    a4 = bitestemp[i + 24: i + 26]
    b4 = bitestemp[i + 29:i + 31]
    x = (a1 + b1 + a2 + b2 + a3 + b3 + a4 + b4).replace(" ", "0")
    bites.append(x)
    i += 8
y = 0
w = ""
numbers = []
while y < len(bites):
    w = bites[y]
    numbers.append(int(w,2))
    y += 1
print(len(numbers) , " total numbers.")

n2 = []
n3 = []
n5 = []
n7 = [] 
v = 0

while v < len(numbers):
    if numbers[v] % 2 == 0:
        n2.append(numbers[v])
    if numbers[v] % 3 == 0:
        n3.append(numbers[v])
    if numbers[v] % 5 == 0:
        n5.append(numbers[v])
    if numbers[v] % 7 == 0:
        n7.append(numbers[v])
    v += 1

print(len(n2) , " numbers that can be divided perfectly by 2," , len(n2)/len(numbers) * 100 , "%")
print(len(n3) , " numbers that can be divided perfectly by 3," , len(n3)/len(numbers) * 100 , "%")
print(len(n5) , " numbers that can be divided perfectly by 5," , len(n5)/len(numbers) * 100 , "%")
print(len(n7) , " numbers that can be divided perfectly by 7," , len(n7)/len(numbers) * 100 , "%")
input()