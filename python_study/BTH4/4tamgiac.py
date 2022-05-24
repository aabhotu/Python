import math
class tamgiac:
    def __init__(self,a,b,c):
        self.a= a
        self.b= b
        self.c= c
        return
class tamgiacdeu(tamgiac):
    def chuvi(self):
        chuvi= self.a*3
        return chuvi
    def dientich(self):
        chieucao= math.sqrt(((self.a)**2-(self.a/2)**2))
        dientich= ((0.5*self.a)*chieucao)
        return dientich
class tamgiacvuong(tamgiac):
    def chuvi(self):
        chuvi = self.a*self.b*self.c
        return chuvi
    def dientich(self):
        chieucao= math.sqrt(((self.a)**2-(self.a/2)**2))
        dientich= ((0.5*self.a)*chieucao)
        return dientich
class tamgiaccan(tamgiac):
    def chuvi(self):
        chuvi = self.a*self.b*self.c
        return chuvi
    def dientich(self):
        chieucao= math.sqrt(((self.a)**2-(self.a/2)**2))
        dientich= ((0.5*self.a)*chieucao)
        return dientich


        
def kiemtratamgiac(a,b,c):
    if(a+b>c and b+c>a and a+c>b):
        return True
    else:
        return False
def kiemtratamgiacdeu(a,b,c):
    if(a==b==c):
        return True
    else:
        return False
def kiemtratamgiacvuong(a,b,c):
    if(a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2):
        return True
    else:
        return False
def kiemtratamgiaccan(a,b,c):
    if(a==b or b==c or c==a):
        return True
    else:
        return False
    
   





a= float(input("nhap canh a:"))
b= float(input("nhap canh b:"))
c= float(input("nhap canh c:"))
if kiemtratamgiac(a,b,c) == True:
    if kiemtratamgiacdeu(a,b,c) == True:
        deu=tamgiacdeu(a,b,c)
        print("chu vi tam giac deu la:", deu.chuvi())
        print("dien tich tam giac la:", deu.dientich())
        
        
    else:
        print("Khong phai tam giac deu")
        if kiemtratamgiacvuong(a,b,c)==True:
            vuong=tamgiacvuong(a,b,c)
            print("chu vi tam giac vuong la", vuong.chuvi())
            print("dien tich tam giac vuong la", vuong.dientich())
        else:
            print("khong phai la tam giac vuong")
            if kiemtratamgiaccan(a,b,c)==True:
                can=tamgiaccan(a,b,c)
                print("chu vi tam giac can la", can.chuvi())
                print("dien tich tam giac can la", can.dientich())
                
            else:
                print("khong phai tam giac can")
    
        
else:
    print("khong phai la tam giac ")




        
    
        
    
