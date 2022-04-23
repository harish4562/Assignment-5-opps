class power:
    def __init__(self,x,n):
        self.n=n
        self.x=x
    def cal(self):
        print(self.x**self.n)

a=int(input('x:'))
b=int(input('n:')) 
pow1 = power(a,b)       
pow1.cal()