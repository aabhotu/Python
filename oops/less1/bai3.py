class product:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.price = 0
        self.quantity = 0

    def input(self):
        self.code = input('Nhap ma san pham: ')
        self.name = input('Nhap ten san pham: ')
        self.price = int(input('Nhap gia: '))
        self.quantity = int(input('Nhap so luong: '))

    def output(self):
        print('{:<10}{:<10}{:<10}{:<10}'.format(
            'code', 'name', 'price', 'quantity'))
        print('{:<10}{:<10}{:<10}{:<10}'.format(
            self.code, self.name, self.price, self.quantity))


product1 = product()
product1.input()
product1.output()
