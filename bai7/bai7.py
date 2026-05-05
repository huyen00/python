# Input và output
# 7.1.Fancier output fomatting (định djang đầu ra đẹp hơn)
year = 2026
name = "Huyền"
old = input("Nhập năm sinh của bạn: ")
print(f'Năm {year}, {name} đã {year-(int(old))} tuổi')
# str.fomat()
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes/total_votes
x = '{:-9} YES votes {:2.2%}'.format(yes_votes,percentage)
print("percentage= ", x)
# -------------------
# 7.1.1: Formatted string literals (f-string)
import math
print(f'làm tròn giá trị pi với 4 chữ số thập phân: {math.pi:.4f}')
# độ rộng
table = {'Sjoerd': 41274, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# --------------

# Modifier	Ý nghĩa
# !s	    dùng str()
# !r	    dùng repr()
# !a	    dùng ascii()
# ------------------
# 7.1.2 The string format() method (có thể truyền vào như tham sốt của hàm .format())
# đóng vai trò tham chiếu đến vị trí của đối tường truyền avfo
print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam
# -----------
# Tham chiếu qua từ khóa truyền vào
print("This {food} is {adjective}.".format(food='spam', adjective='absolutely horrible'))
# các đối số vị trí và đối số từ khóa có thể được kết hợp tùy ý
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.
# ---------------------------------
# 7.1.3:Manual string formatting (Định dạng chuỗi thủ công)
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end =' ')
    print(repr(x*x*x).rjust(4))
# --------------
# phương thức str.zfill(): là method của chuỗi dùng để thêm số 0 và bên trái để đạt độ dài tối thiểu width
# nếu có dâu +,- thì chèn số 0 sau dấu
m = '12'.zfill(5)
print("zfill:", m)
# ==========-===========
# 7.1.4: Old string formatting (định dạng  chuỗi cũ)
#  format: chuỗi chứa các kí  hiệu định dạng (%...)
# values: giá trị sẽ được chèn vào
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.
# giải thích
# Phần	Ý nghĩa
# %	    bắt đầu format
# 5	    độ rộng tối thiểu = 5 ký tự
# .3	3 chữ số thập phân
# f	    kiểu float
# =============================
# 7.2: Reading and writing files (ĐỌc và ghi tệp tin)
f = open('workfile', 'w', encoding="utf-8")
# Thâm số đầu tiên : chuỗi chứa tên tệp, tham số thứ 2: chuỗi khác chứa 1 vài ký tự mô tả cách thứuc sử dụng (r:chỉ đọc, w: chỉ ghi)
print("mở", f)