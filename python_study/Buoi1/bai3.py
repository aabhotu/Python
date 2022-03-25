import math
canh1 = int(input())
canh2 = int(input())
canhHuyen = math.sqrt(canh1**2 + canh2**2)
print('canh huyen: ', canhHuyen)
print('chu vi: ', str(canh1 + canh2 + canhHuyen))
print('dien tich: ', str(canh1 * canh2 / 2))
goc1 = math.degrees(math.acos(canh1/canhHuyen))
goc2 = 90 - goc1
print('goc doi canh1: ' + str(goc1))
print('goc doi canh2: ' + str(goc2))
