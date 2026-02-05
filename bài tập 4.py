i = input("mời nhập chữ số của bạn")
tong = i.count("1") + i.count("2") * 2 + i.count("3") * 3 + i.count("4") * 4 + i.count("5") * 5 + i.count("6") * 6 + i.count("7") * 7 + i.count("8") * 8 + i.count("9") * 9
print("tổng các chữ số trong chữ số của bạn là",tong)
#cách 2
i = input("mời nhập số của bạn: ")
tong = 0

for ch in i:
    if ch != "." and ch != "-":
        tong = tong + int(ch)

print("tổng các chữ số là", tong)




