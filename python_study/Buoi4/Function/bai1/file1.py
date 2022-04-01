# tạo 1 file chứa các hàm ktra 1 số có phải là số chính phương ko?
# số có là số nguyên tố ko, số có là số đảo ko.
# tạo file 2 cho phép nhậ 1 list các số nguyên. đêm và tính trung bình cộng
# các số chính phương , nguyên tố số đảo trong list.


def SoChinhPhuong(a):
    if a < 0:
        return False
    else:
        for i in range(1, a+1):
            if i**2 == a:
                return True
                break


def soNguyenTo(a):
    if a < 2:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


def SoDao(a):
    try:
        return int(str(a)[::-1]) == a
    except:
        return False
    # soNghichDao = 0
    # temp = a
    # while temp != 0:
    #     soNghichDao = soNghichDao*10+temp % 10
    #     temp = temp//10
    # if soNghichDao == a:
    #     return True
    # else:
    #     return False


# def soDao(a):
#     soDao = ''
#     while a != 0:
#         soDao += str(a % 10)
#         a = a//10
#     return int(soDao)
