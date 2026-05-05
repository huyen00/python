# import bai6
# gán hàm fib vào biến f
# f = bai6.fib
# f(4)
# a=0, b=1-> print a=0 
#  a,b =b, a+b -> a=1, b=1
# l2: a=1, b=1 -> print a=1
# a,b = a, a+b -> a=1, b= 1+1=2
# l3: a =1, b=2 -> print a=1
# a,b=b, a+b -> a=2, b=1+2 =3
# l4: a= 2, b= 3 -> print a =2
# a,b =b, a+b -> a= 3, b= 2+3=5
# l5: a=3, b=5 -> print a=3
# a,b =b, a+b => a=5. b= 3+5 =8
# l6: a=5 > n=4-> stop
# kq:0 1 1 2 3
# ---------------------------
# 6.1
# import trược tiếp hàm fib trong module bài 6
from bai6 import fib, fib2
# import bai6 as fib
# from bai6 import fib as fabonacci
import importlib

import bai6
importlib.reload(bai6)
# fib(6)
# fib2(5)
# fabonacci(6)
import random
x = random.randint(3,1000)
print("x=",x)
print(random.__file__) # kiểm tra in đường dẫn của module random
# ------------------------------
# 6.1.3: compiled Python files (tập tin được biên dịch)
# khi chạy chương trình --> compile chạy --> tạo ra file .pyc --> chạy nhanh hơn (.pyc không giúp code chạy nhanh hơn mà chỉ giúp load nhanh hơn, giúp quản lý nhiều version)
# ------------------------------
# 6.2 standard modules (các module chuẩn)
# một số module chuẩn mà python có sẵn: math, os, sys, random, datetime, re, json, csv, ...
import sys
print(sys.builtin_module_names) # kiểm tra các module có sẵn trong python
print("sys.version=",sys.version)
print("sys.path=", sys.path)
sys.ps1="Hello: " # thay đổi dấu nhắc lệnh mặc định của python
print("sys.ps1=", sys.ps1)
# sys.ps1 : primpt chính
# sys.ps2: prompt phụ
# ------------------------------
# 6.3: The dir() Function (hàm dir(): liệt kê tất cả các thuộc tính của function)
di = dir(fib)
print("dir(fib)=", di)
a=10
b="hello"
print("dir(a)=", dir(a))
print("dir(b)=", dir(b))
print("dir(10)= ", dir(10))
# ------------------------------
# 6.4:Packages(gói): 
# import trực tiếp function trong module con của package
# from utils.string_utils import * # utils là package, string_utils là module con, * là tất cả các function trong module con
from utils.string_utils import *
print(to_upper("hello world"))
print(count_chars("hello world"))
# đối với version python >3.3 thì không cần file __init__.py trong thư mục package nữa, nhưng nếu có thì nó sẽ được chạy khi import package đó

