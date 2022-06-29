class A:
    def __init__(self,x,y):
        pass

class B(A):
    def calculate_power(self):
        pass

if __name__=="__main__":
    x,y =[int(n) for n in input("Enter 2 integers").split()]
    obj=B(x,y)
    print(obj.calculate_power())
