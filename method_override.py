class Super():
    def calculate(self,x,y):
        pass

class Sub(Super):
    def calculate(self,x,y):
        pass

if __name__=="__main__":
    sb=Sub()
    print(sb.calculate(x,y))
