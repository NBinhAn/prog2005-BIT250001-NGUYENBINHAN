def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
number = int(input("Nhập một số nguyên: "))
print(is_even(number))
