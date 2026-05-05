# căn lề
p = "{:>10}".format("hi")
print("căn phải:",p )
# căn trái
t = "{:<10}".format("hi")
print("căn trái:", t)
# căn giữa
g = "{:^10}".format("hi")
print("căn giữa:", g)
# thêm kí tự đặc biệt
kitu = "{:#^10}".format("hi") # thêm kí tự #
print("Thêm kí tự đặc biệt:", kitu)
# --------------------------------
# số nguyên
songuyen = "{:d}".format(10)
print("SỐ nguyên:", songuyen)
# thêm số 0
y = "{:03d}".format(10) # thêm số 0 vào cho đủ 3 số # 010
print("Thêm số 0:", y)
# ----------------------------------
# Sô thực (float)
x = "{:.3f}".format(3.24259) # 3.243
print("Số thực 3 chữ số thập phân", x)
# số thựuc làm tròn
z = "{:.0f}".format(3.541526)
print("Số thựuc làm tròn:", z)
# rộng 10 kí tự
j = "{:10.2f}".format(3.14)
print("Rộng 10 kí tự:", j)
# ---------------------------
# dâu phẩy và phân cách
a = "{:,}".format(10000000)
print("ĐỊnh dạng số có dấu phảy:", a)
# --------------------------------
# phần trăm %
b = "{:.5%}".format(0.2345) # .5& là sau dấu phảu có 5 số 
print("Phần trăm của 0.2345 là:", b)
# ---------------------
# str():hiển thị dễ đọc
# repr(): hiển thị dạng code
s = "hello\nworld"
print(str(s))  # hello
                # world                    
print(repr(s)) #'hello\nworld'
x = 10 * 3.25
y = 200 * 200
s1 = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(str(s1))                    
print(repr(s1))