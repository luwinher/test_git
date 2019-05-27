#
"""Q15:利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。"""

score = int(input("请输入该同学分数："))
S = 'A' if (score>=90) else ('B' if (score>=60) else 'C')
print(S)


