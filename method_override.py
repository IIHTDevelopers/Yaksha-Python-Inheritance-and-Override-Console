class Super():
    def calculate(self,x,y):
        pass

class Sub(Super):
    def calculate(self,x,y):
        pass

if __name__=="__main__":
    sb=Sub()
    x,y =[int(n) for n in input("Enter 2 integers").split()]
    print(sb.calculate(x,y))
