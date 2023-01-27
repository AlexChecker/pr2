def getVicYear(year,vicyear):
    while True:
        if vicyear>year: return False
        if year == vicyear: return True
        vicyear +=4

vicyear=2000
year = int(input())
yearres=0
months=[31,0,31,30,31,30,31,31,30,31,30,31]

if getVicYear(year,vicyear):
    months[1]=29
else:
    months[1]=28

for month in months:
    num=1
    res=0
    while num<=month:
        if num<10:
            res+=num
        else:
            num1=int(num/10)
            num2=num%10
            res+=num1+num2
        num+=1
    num=0
    print(res)
    yearres+=res

print(yearres)

