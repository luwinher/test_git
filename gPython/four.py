#

monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
datestr = input("请输入日期(格式：yyyy-mm-dd)：")
date = datestr.split('-')
#print(date)
year = int(date[0])
month = int(date[1])
day = int(date[2])
if month > 12 or day > 31:
    print("date is error!")
    exit(-1)
if year%100==0:
    if year%400==0:
        monthlist[1]=29
elif year%4==0:
    monthlist[1]=29
print(monthlist[1])
days = 0
for m in range(1,12):
    if month > m:
        days += monthlist[m-1]
    else:
        days +=day
        break

print(datestr+"是今年的第"+str(days)+"天")
