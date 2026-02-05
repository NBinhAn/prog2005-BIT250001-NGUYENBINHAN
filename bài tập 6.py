def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
n = int(input("Nhập một số nguyên không âm: "))
if n < 0:
    print("Không thể tính giai thừa cho số âm.")
else:
    print(f"Giai thừa của {n} là: {giai_thua(n)}")
