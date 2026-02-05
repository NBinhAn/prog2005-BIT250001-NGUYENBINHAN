
n = int(input("Nhập một số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    tong_so_le = 0
    for i in range(1, n + 1, 2):
        tong_so_le += i

    print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_so_le}")
