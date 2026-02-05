
def tinh_tong(n):
    if n == 1:
        return 1
    return n + tinh_tong(n - 1)
n = int(input("Nhập một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print(f"Tổng các số từ 1 đến {n} là: {tinh_tong(n)}")
