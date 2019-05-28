#
"""Q17:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。"""

class Check(object):
    context = ''
    alpha = 0
    digit = 0
    space = 0
    other = 0

    def __init__(self,context):
        self.context = context

    def chcontext(self):
        for c in self.context:
            if c.isalpha():
                self.alpha +=1
            elif c.isdigit():
                self.digit +=1
            elif c.isspace():
                self.space +=1
            else:
                self.other +=1

    def showcheck(self):
        print("您输入的内容是：%s" %self.context)
        print("其中,字母(%d),数字(%d),空格(%d),其他(%d)." % (self.alpha,self.digit,self.space,self.other))

con = input("请输入你要统计的内容: ")
ch = Check(con)
ch.chcontext()
ch.showcheck()
