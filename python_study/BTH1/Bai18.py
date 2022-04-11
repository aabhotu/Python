canh1 = float(input('Nhap canh1: '))
canh2 = float(input('Nhap canh2: '))
canh3 = float(input('Nhap canh3: '))

if(canh1 + canh2 <= canh3 or canh1+canh3 <= canh2 or canh2+canh3 <= canh1):
    print('Khong phai tam giac')
else:
    if(canh1 == canh2 == canh3):
        print('Tam giac deu')
    elif(canh1 == canh2 or canh1 == canh3 or canh2 == canh3):
        print('Tam giac can')
    elif(canh1**2+canh2**2 == canh3**2 or canh1**2+canh3**2 == canh2**2 or canh2**2+canh3**2 == canh1**2):
        print('Tam giac vuong')
    else:
        print('Tam giac thuong')
