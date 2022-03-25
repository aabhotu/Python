class books:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.author = ''
        self.page = 0
        self.price = 0

    def input(self):
        self.code = input('code:')
        self.name = input('name:')
        self.author = input('author:')
        self.page = int(input('page:'))
        self.price = int(input('price:'))

    def output(self):
        print('{:<10}{:<15}{:<20}{:<10}{:<10}'.format(
            'code', 'name', 'author', 'page', 'price'))
        print('{:<10}{:<15}{:<20}{:<10}{:<10}'.format(
            self.code, self.name, self.author, self.page, self.price))


book = books()
book.input()
book.output()
