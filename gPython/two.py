#

profit = 0
award = 0

profit=input("请输入本月利润：")
print("本月利润："+profit)
profit = int(profit)
if profit < 100000:
    award = profit*0.1
elif profit < 200000:
    award = 100000*0.1+(profit-100000)*0.075
elif profit < 400000:
    award = 100000*0.1+100000*0.075+(profit-200000)*0.05
elif profit < 600000:
    award = 100000*0.1+100000*0.075+200000*0.05+(profit-400000)*0.03
elif profit < 1000000:
    award = 100000*0.1+100000*0.075+200000*0.05+200000*0.03+(profit-600000)*0.015
else:
    award = 100000*0.1+100000*0.075+200000*0.05+200000*0.03+400000*0.015+(profit-1000000)*0.01

print("本月奖金："+str(int(award)))
