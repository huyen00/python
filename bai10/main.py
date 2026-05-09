# 10.Brief tour of the standard library (thư viện có sẵn trong python)
# 10.1: Operating system interface (Giao diện hệ điều hành os)
# ---- module
import os
from urllib.request import urlopen
print(os.getcwd()) #in ra thư mục làm việc hiện tại của project
os.chdir('/python/python') #thay đổi thư mục làm việc hiện tại
# os.system('mkdir tody1') # tạo 1 thư mục mới
print("thư mục làm việc hiện tại: ", os.getcwd())
print(os.listdir()) # trả về danh sách các file và thư mục trong thư mục hiện tại
# print("các hàm trong module os là:", dir(os)) # trả về hàm trong ds của module os
# os.mkdir("huyen") # tạo thư mục mới có tên huyen
# os.rmdir("Thư mục được tạo mới") # xóa thư mục 
# ---------
import shutil # cung cấp interface cấp cao hơn để quản lý file/thư mục dễ hơn.
shutil.copyfile('D:/python/python/bai10/main.py', 'D:/python/python/bai10/text.txt')
shutil.move('D:/python/python/bai10/text.txt', 'D:/python/python/bai10/new_text.txt') # di chuyển file sang 1 thư mục/file khác

# shutil.rmtree("tody1") # xóa thư mục tody1 cùng tất cả nội dung bên trong
# ==============================
# 10.2: File wildcards (module glob: dùng để tìm file, lọc file theo pattern)
# Ký tự	    Ý nghĩa
# *	        mọi ký tự
# ?	        1 ký tự
# []	    nhóm ký tự

import glob

f= glob.glob('*.py')
print("các file có đuổi .b là:", f) #list các file có đuổi .py trong thư mục làm việc hiện tại/ sử dụng os.chdir để thay đổi thư mục làm việc và lọc tìm file
y = glob.glob('READM?.md') # tìm đúng 1 kí tự cuối cùng có tên file trùng với
print("file có tên trùng với bai?.py",y)

Z = glob.glob("bai[45].py") # tìm file có bắt đầu là "bai", [45]: chỉ được là 4 hoặc 5, kết thúc bằng .py
print("tìm file có []:", Z)
# ==================================
# 10.3: Command-line arguments ( tham số dòng lệnh)
#  Phần này nói về cách python nhận dữ liệu khi chạy chương trình từ terminal/cmd
# --- sys.argv
import sys
sys.argv
print("sys.argv:", sys.argv) #['bai10/main.py','one','two','three']: argv[0]: tên file python, argv[1]:one, argv[2]:two, argv[3]:three
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# print("a+b:",a+b) # 13
# -------- argparse(module dùng để parse arguments/ validate kiểu dữ liệu/ tạo help command)
import argparse
# parser = argparse.ArgumentParser(prog ='main', description='shơ tai liệu') # tạo đổi tượng parser để đọc tham số command line
# parser.add_argument("filenames", nargs = '+') # phải có ít nhất 1 giá trị và có thể nhièu hơn 1
# parser.add_argument('-l','--lines', type =int, default=10)
# args = parser.parse_args() #phân tích command line và trả về object kiểu NameSpace:args = Namespace( filenames=['a.txt', 'b.txt'],lines=10)
# print("args:",args) # câu lệnh chạy: python bai10/main.py -l 20 a.txt b.txt
# print("args.file", args.filenames)
# print("args.line", args.lines)

# ==============================

# 10.4: Error output redirection and program termination (Chuyển hướng output lỗi và kết thúc chương trình)
# module sys cũng có các thuộc tính: stdin/stdout/stderr
# + stderr: hiển thị warning/hiển thị error message kể cả khi stdout đã bị redirect
#  + stdin: dữu liệu nhập vào
#  + stdout: output bình thường
#  + stderr: output lỗi/ cảnh báo
#  + sys.exit():kết thúc chương trình

sys.stdout.write("Hello\n")
sys.stderr.write("warning, log file not found starting a new one")

print("Đây là output thường")
sys.stderr.write("Đây là warning\n")

# =====================================

# 10.5:String pattern matching (xử lý mẫu chuỗi: module re): cung cấp các công cụ Regular Expression để xử lý chuỗi nâng cao
# tìm kiếm/thay thế/kiểm tra pattern
import re
r= re.findall(r'\bo[a-z]*', 'which foot or hand fell fastest')
print("Tifm tất cả f:", r)
# re.findall(): trả về tất cả phần match
# 🧠 Phân tích regex
# Regex	    Ý nghĩa
# \b	    bắt đầu từ đầu từ
# f	        chữ f
# [a-z]	    ký tự a-z
# *	        0 hoặc nhiều lần
# (\b[a-z]+)    lấy 1 từ
# \1            lặp lại từ trước đó

# ----------- re.sub(): dùng để thay thế bằng regex
sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') # từ the the --> the
print("thay thế:", sub)

# regex ---------- ý nghĩa
# .         mọi kí tự
#  *        0+ lần
#  +        1+ lần
# ?         0 hoặc 1
#  [a-z]    kí tự
#  \d       số
# \w        chữ + số
# \s        khoảng trắng
# ^         bắt đầu
# $         kết thúc

# ----- module re
# findall: tìm tất cả kết quả match
# search:tìm kiếm match đầu tiên
# match: kiểm tra pattern ở đầu chuỗi
# sub : thay thế

# =============================

# 10.6: Mathematics (module toán học)
import math #cung cấp các hàm toán học

# Hàm	    Ý nghĩa
# sqrt()	căn bậc hai
# pow()	    lũy thừa
# sin()	    sin
# cos()	    cos
# log()	    log
# ceil()	làm tròn lên
# floor()	làm tròn xuống

import random #tạo dữ liệu ngẫu nhiên

# Hàm           Ý nghĩa
# choice         chọn 1 phần tử
# sample()       chọn nhiều phần tử
# random()       số thực random
# randint(a,b)   Số nguyên
# shuffle()      trộn list

import statistics
# Hàm           ý nghĩa
# mean()        trung bình
# median()      trung vị
# mode()        giá trị xuất hiện nhiều
# variance()    phương sai
# stdev()       độ lệch chuẩn

# ====================================

# 10.7: internet access(truy cập internet)
# lấy dữ liệu từ internet
# gửi email
# làm việc với giao thức mạng

# -----------

# + urllib.request (dùng truy cập url/ tải dữ liệu từ web)
# from urllib.request import urlopen
# with urlopen('https://docs.python.org/3/') as respon:
#     for line in respon:
#         line = line.decode()
#         if 'updated' in line:
#             print("line.rstrip()", line.rstrip())
# print("respon", respon)

# 🧠 Ý nghĩa
# Tham số	Ý nghĩa
# sender	email gửi
# receiver	email nhận
# message	nội dung mail

with urlopen('https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching') as respon:
    print("respon:", respon)
    # print("respon.read():", respon.read()) # trả về nội dung của trang web
    print("trạng thái trả về từ url:", respon.status) 
    print("header trả về từ url",respon.headers) # trả về header của trang web
    print("get url:", respon.geturl())


# reponse: trả về một đối tượng HTTPResponse có các thuộc tính:
# + status: mã trạng thái HTTP (200, 404, 500,...)
# + read(): trả về nội dung của trang web
# + headers: trả về header của trang web
# + geturl(): trả về url của trang web
# header: trả về thông tin mô tả response HTTP: + metadata
                                            # + cache info/security info / content info

# ------------------\
# Gửi email bằng module smtplib

# import smtplib
# from email.mime.text import MIMEText
# # email người gửi
# sender = 'hoanghuyenn2k@gmail.com'
# # mật khẩu ứng dụng email
# password = 'gavmwinbflkqbsri'
# # email người nhận
# receiver = 'hungvietnguyen6241@gmail.com'
# # nội dung email
# # message = MIMEText('Xin chào Việt Hùng, tớ là HH')
# html = """
# <h2>Xin chào Việt Hùng</h2>
# <p><b>Tớ là HH.</b></p>
# <p>Chúc cậu một ngày vui vẻ ❤️😘</p>
# <p>Cấu đứt cậu cái ❤️😘
#  """
# message = MIMEText(html, "html")
# # tiêu đề email
# message['Subject'] = 'Bé iu gửi VH'
# message['From'] = sender
# message['To'] = receiver
# # gửi email
# try:
# # kêt nối smpt smail
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls() # khởi động TLS để bảo mật kết nối
#     # handshake lại sau TLS
#     server.ehlo()
#     server.login(sender, password) # đăng nhập vào tài khoản email
#     server.send_message(message) # gửi email
#     print("Gửi thành công")
# except Exception as e:
#     print("Gửi thất bại:", e)
# finally:
#     server.quit() # đảm bảo đóng kết nối email dù có lỗi hay không

# =====================================
# 10.8: Dates and times (module datetime)
import datetime as dt
today = dt.date.today()
print("ngày hiện tại:", today.strftime("%m-%d-%y"))
last_week = today - dt.timedelta(days=7)
print("ngày tuần trước:", last_week.strftime("%m-%d-%y"))

# %m	tháng
# %d	ngày
# %y	năm 2 số
# %Y	năm 4 số
# %b	tên tháng ngắn
# %B	tên tháng đầy đủ
# %A	tên thứ

# =====================================

# 10.9: Data archiving and compression (nén và lưu trữ dữ liệu)
# có sẵn nhiều module để: 
# + zlib: nén dữ liệu
# + gzip: giải nén dữ liệu
# + zipfile: làm việc với file zip
# + tarfile: làm việc với file tar

import zlib
s = b'witch which has which witches wrist watch witch which has which witches wrist watch'
print("độ dài ban đầu:", len(s))
# nén dữ liệu
t = zlib.compress(s)
print("độ dài sau khi nén:", len(t))

# giải nén dữ liệu
z = zlib.decompress(t)
print("dữ liệu sau khi giải nén:", len(z))
print("dữ liệu sau khi giải nén:", zlib.decompress(t))

# các module nén phổ biến
#  Module        Định dạng
# zlib           nén raw
# gzip           .gz
# bz2            .bz2
# lzma           .xz
# zipfile        .zip
# tarfile        .tar

# ======================================

# 10.10: Performance measurement (Đo hiệu năng chương trình)
#  python có các công cụ để :
# + Đo tốc độ code
# + so sánh cách viết
# + tìm đoạn code chậm

# module đo thời gian cạy code
from timeit import Timer
tg= Timer('t=a; a=b', 'a=1;b=2').timeit() # đo thời gian chạy code
print("thời gian chạy code:", tg)

t = Timer('sum(range(1000))')
print("thời gian chạy sum:", t.timeit())
# *** cấu trúc Timer: Timer(statement, setup) *****
# statement: code cần đo thời gian chạy
# setup: code chuẩn bị trước khi chạy statement (không được tính vào thời gian chạy)
# timeit(): chạy statement nhiều lần và trả về thời gian trung bình

#  -------------------------------------
# profile: dùng cho chương trình lớn/ phân tích toàn chương trình
import cProfile
def test():
    total = 0
    for i in range(100000):
        total +=i
cProfile.run('test()')

# -----------------------------------------
# pstats: phân tích kết quả profile chi tiết hơn


# =====================================

# 10.11: Quality control (Kiểm soát chất lượng phần mềm)
# + doctest: test đơn giản trong docstring
# + unittest: framework test đầy đủ

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) /len(values)
# docstring: """...""" mô tả function

# >>> print(average([20, 30, 70]))
#  40.0
# --> đây là test. >>>: lệnh python, 40.0 kết quả mong đợi
# --------------------------
# chạy test
import doctest
doctest.testmod()
# python sẽ: - quét tất cả docstring. - tìm >>> - chạy thử. - so sánh kết quả -->nếu đúng: không hiện gì, nếu sai: python báo lỗi test failed
# test thử trường hợp failed bằng cách đưa kết quả sai vào docstring
def add(a,b):
    """Trả về tổng của a và b
    >>> add(2,3)
    6
    >>> add(-1,1)
    0
    """
    return a+b
# print(add(1,2))
doctest.testmod()
# -------------------------------
# unittest: đây là framework test chuyên nghiệp hơn
import unittest

class TestStatisticalFunctions(unittest.TestCase): # class chứa test
    def test_average(self): # mọi hàm bắt đầu bằng test_ sẽ được chạy khi chạy unittest
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(average([-1, 1]), 0.0)

# ===============================
# 10.12: Batteries included (Python có sẵn nhiều thư viện để làm việc với nhiều lĩnh vực khác nhau như: khoa học dữ liệu, machine learning, web development,...)
# 4.csv: file excel text/ tạo-đọc-ghi file
import csv
with open("bai10/data.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'New York'])

# đọc csv
with open("bai10/data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print("row:", row)

# --------------------------------
# 6.sqlite3: lưu trong file/không cần server
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (name TEXT)")
cursor.execute("INSERT INTO users VALUES ('Alice')")
conn.commit()
# query dữ liệu
cursor.execute("SELECT * FROM users")
print("dữ liệu trong bảng users:", cursor.fetchall())

