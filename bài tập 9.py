
n = int(input("Nhập một số nguyên dương có 5 chữ số: "))
if n < 10000 or n > 99999:
    print("Vui lòng nhập đúng một số nguyên dương có 5 chữ số.")
else:
    max_digit = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit > max_digit:
            max_digit = digit
        temp //= 10
    print(f"Chữ số lớn nhất trong số {n} là: {max_digit}")
