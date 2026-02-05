
a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
if a <= 0 or b <= 0:
    print("Vui lòng nhập hai số nguyên dương.")
else:
    while b != 0:
        a, b = b, a % b

    print("Ước số chung lớn nhất là:", a)
