def getVicYear(year):
    while True:
        if vicyear>year: return False
        if year == vicyear: return True
        vicyear +=4

vicyear=2000
year = int(input())

months=[]

months.append(31)
if getVicYear(year):
    months.append(29)
else:
    months.append(28)
months.append(31)
months.append(30)
months.append(31)
months.append(30)
months.append(31)
months.append(31)
months.append(30)
months.append(31)
months.append(30)
months.append(31)








