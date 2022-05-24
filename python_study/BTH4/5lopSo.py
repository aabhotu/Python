class so():
    def __init__(self, giaTri):
        self.giaTri=giaTri
        return 
    def check(self):
        if self.giaTri%1==0:
            return True
        else:
            return False
    def chan(self):
        if self.check()==True:
            if self.giaTri%2==0:
                return True
            else: 
                return False
        else:
            return False
    def le(self):
        if self.check()==True:
            if self.giaTri%2==0:
                return False
            else: 
                return True
        else:
            return False
    def am(self):
        if self.check()==True:
            if self.giaTri<0:
                return True
            else: 
                return False
        else:
            return False
    def duong(self):
        if self.check()==True:
            if self.giaTri>0:
                return True
            else: 
                return False
        else:
            return False
    def nguyenTo(self):
        if self.check()==True:
            if self.giaTri<2:
                return False
            else:
                dem=0
                while i<self.giaTri:
                    if self.giaTri%i==0:
                        dem=dem+1
                        i=i+1
                if dem==0:
                    return True
                else:
                    return False
        else:
            return False
    def hoanThien(self):
        if self.check()==True:
            tong=0
            if self.giaTri<=0:
                return False
            else:
                for i in range(1, self.giaTri):
                    if self.giaTri%i==0:
                        tong=tong+i
                if tong==self.giaTri:
                    return True
                else:
                    return False
        else:
            return False
    def doiXung(self):
        if self.check()==True:
            N=str(self.giaTri)
            N1=N[::-1]
            if N==N1:
                return True
            else:
                return False 
        else:
            return False
