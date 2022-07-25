## Bài 1:

Viết chương trình nhập vào điểm tổng kết của một học sinh và in ra xếp loại cho học sinh đó với quy định:

    - Xếp loại giỏi nếu tổng điểm từ 8.00 trở lên.
    - Xếp loại khá nếu tổng điểm từ 7.00 tới cận 8.00.
    - Xếp loại trung bình nếu tổng điểm từ 5.00 tới cận 7.00.
    - Còn lại, xếp loại yếu.

## Bài 2:

Viết chương trình nhập vào một số nguyên n, sau đó tính giá trị biểu thức:

![Đề bài 2] (D:\vscode\python\Python_HIT\BTVN2\bai2.png)

## Bài 3: Không bắt buộc

Thiết kế một game console cơ bản cho hai người chơi với các yêu cầu sau:

    - Đầu mỗi round game yêu cầu nhập hai số nguyên dương n và k với n>k ( game phải check điều kiện nếu người dung nhập không đúng thì yêu cầu nhập lại)
    - Trò chơi chia làm các turn liên tiếp nhau, đến lượt của mình game yêu cầu người chơi nhập từ bàn phím một số nguyên dương trong đoạn [1 , min(n,k)] ( game phải check điều kiện nhập). Sau khi nhập chương trình sẽ trừ n đi số mà người chơi vừa nhập.
    - Đến lượt của mình người chơi nào không thể đi tiếp sẽ thua, round kết thúc và game thông báo người thắng round đó
    - Cuối mỗi round game thông báo người chơi có muốn tiếp tục không, người chơi nhập “YES” để tiếp tục “NO” để dừng trò chơi nếu nhập khái thì yêu cầu nhập lại
    - Sau khi game dừng lại thì in ra thống kê của game với các yêu cầu sau
        - Người chơi nào thắng chung cuộc (tổng số round thắng lớn hơn)
        - In ra số thứ tự các round mà người thắng chung cuộc đã thắng
        - Trường hợp hai người chơi có số round thắng bằng nhau thì người chơi nào phạm luật nhiều hơn sẽ thua (số lần phạm luật được tính bằng số lần nhập sai yêu cầu khi đến turn của mình)
        - Trường hợp số lần phạm luật hai bên bằng nhau thì thông báo hai đối thủ hoà

<strong>Yêu cầu này không bắt buộc:</strong> Các bạn có thể làm cho con game của mình đẹp hơn bằng cách clear màn hình sau mỗi lần nhập( tham khảo os.system(‘cls’) )

## Bài 4:

    1.Tính S(n) = 1 + 2 + 3 + … + n
    2.Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)
    3.Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1
    4.Tính S(n) = x + x^2 + x^3 + … + x^n
    5.Viết chương trình giải và biện luận phương trình bậc nhất ax + b = 0
    6.Tìm số nguyên dương n nhỏ nhất sao cho 1 + 2 + … + n > 10000
    7. Hãy sử dụng vòng lặp for để xuất tất cả các ký tự từ A đến Z
    8.Viết chương trình kiểm tra 1 số có phải là số nguyên tố hay không

## Bài 5:

    Nhập vào 1 chuỗi có dạng dd/mm/yyyy##
    dd: biểu thị của ngày (1 - > 31),
    mm: biểu thị của tháng (1 -> 12),
    yyyy biểu thị của năm ( >= 1000) .
    Yêu cầu đếm từ ngày nhập vào đến cuối năm đó có bao nhiêu ngày.
    Đầu vào: 12/05/2001
    Đầu ra: 234
    Giải thích: Từ ngày 12/05/2001 -> 31/12/2001 có 223 ngày.

## Bài 6:

Cho 1 mảng có n số. Nếu tổng số chẵn lớn hơn tổng số lẻ in ra “even”. Nếu tổng số chẵn nhỏ hơn số lẻ in ra “odd”. Nếu bằng nhau in ra “equal “.
Ví dụ:
|Đầu vào|Đầu ra|
|5|odd|
|1 2 3 4 5||

Giải thích: vì 1 +3 +5 > 2+4 nên in ra odd\
Note: Để nhập 1 mảng các số trên 1 dòng như trên thì ta sẽ sử dụng\
arr = list(map(int, input().split()))\
Với ví dụ trên sẽ trả về [1, 2, 3, 4, 5]

## Bài 7: Tính tổng các số ở trong một chuỗi đã cho

|Đầu vào|Đầu ra|
|chitu21anh34kdf-234|-179|
|334-23-342--43|-74|

Giải thích:\
Test 1: ta tìm được những số như sau: 21, 34, -234\
Test 2: ta tìm được những số như sau: 334, -23, -342, -43\
Note: Nếu các bạn thấy khó khi giải quyết vấn đề số âm thì làm chỉ lấy số dương…. vẫn tính nha.
