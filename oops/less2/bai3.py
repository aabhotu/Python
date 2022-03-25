class Product:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.price = 0

    def input(self):
        self.code = input('Nhap ma san pham: ')
        self.name = input('Nhap ten san pham: ')
        self.price = int(input('Nhap gia san pham: '))
        print('------------------------')

    def output(self):
        print("{:<8} {:<20} {:<10}".format(self.code, self.name, self.price))
        # print(' San pham co ma: ', self.code, ', ten: ',
        #       self.name, ', gia: ', self.price)


class ProductList:
    def __init__(self):
        self.code = ''
        self.list = []

    def input(self):
        self.code = input('Nhap ma phieu: ')
        m = int(input('Nhap so luong san pham: '))
        for i in range(m):
            print('san pham thu: ', i + 1)
            p = Product()
            p.input()
            self.list.append(p)

    def output(self):
        print('Phieu co ma: ', self.code)
        print("{:<8} {:<20} {:<10}".format(
            'Ma sp', 'Ten san pham', 'Gia'))
        for i in self.list:
            i.output()


p = ProductList()
p.input()
p.output()
