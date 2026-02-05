
n = int(input("Nhập một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    dao_nguoc = 0
    while n > 0:
        dao_nguoc = dao_nguoc * 10 + (n % 10)
        n //= 10
    print(f"Số sau khi đảo ngược là: {dao_nguoc}")


