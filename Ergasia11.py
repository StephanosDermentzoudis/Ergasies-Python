import math
from urllib.request import Request, urlopen
list1 = []
range1 = "ABCDEFabcdef"

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
cnt = data.decode('UTF-8')
temp = cnt[31 : 95]
temp = temp.upper()
print(temp)
i = 1
a = int(temp, base=16)
list1.append(hex(a))
while i < 20:
    a = (int(temp, base=16) - i)
    list1.append(hex(a))
    i += 1
   
print(list1)

def entropy(string):

    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy

b = ""
b = b.join(list1)
print("The entropy is " , entropy(b))

input()





