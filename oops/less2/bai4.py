class machines:
    def __init__(self):
        self.code = ''
        self.type = ''
        self.state = ''

    def input(self):
        self.code = input('Nhap ma hoa may: ')
        self.type = input('Nhap loai may: ')
        self.state = input('Nhap trang thai may: ')
        print('--------------------')

    def output(self):
        print('{:<10}{:<10}{:<10}'.format(
            self.code, self.type, self.state))


class manages:
    def __init__(self):
        self.code = ''
        self.name = ''

    def input(self):
        self.code = input('Nhap ma hoa quan ly: ')
        self.name = input('Nhap ten quan ly: ')

    def output(self):
        print('{:<10}{:<10}'.format(self.code, self.name))


class room:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.square = 0
        self.list = []
        self.listMa = []

    def input(self):
        self.code = input('Nhap ma phong: ')
        self.name = input('Nhap ten phong: ')
        self.square = int(input('Nhap dien tich: '))
        manage = manages()
        manage.input()
        self.listMa.append(manage)
        n = int(input('Nhap so luong may: '))
        for i in range(n):
            print('may thu: ', i + 1)
            machine = machines()
            machine.input()
            self.list.append(machine)

    def output(self):
        print('Phong co ma: ', self.code)
        print('Ten phong: ', self.name)
        print('Dien tich: ', self.square)
        print('{:<15}{:<10}'.format('Ma quan ly', 'Ten quan ly'))
        for i in self.listMa:
            i.output()
        print('')
        print('{:<10}{:<10}{:<10}'.format('code', 'name', 'state'))
        for i in self.list:
            i.output()


room1 = room()
room1.input()
room1.output()
