# 8. Errors and Exceptions
# 8.1: syntax Errors (Lỗi cú pháp)
# while True:
#     print('Hello world')
# ===============
    # File "<stdin>", line 1
    # while True print('Hello world')
            #    ^^^^^
    # SyntaxError: invalid syntax

# python in ra  dòng bị lỗi
# hiển thị ^ để chỉ vị trí phát hiện lỗi
# <stdin> → code nhập trực tiếp (terminal)
# line 1 → dòng bị lỗi
# ----------------------------------------
# so sánh nhanh
#  Loại lỗi         KHi nào xảy ra
#  Syntax Error     sai cú pháp
#  Runtime Error    Lỗi khi chạy
#  Logic Error      chạy đúng nhưng sai kết quả
# ------> xảy ra trước khi chạy
# ==============================================
# 8.2: Exceptions (Ngoại lệ)
# các exception có sắn trong python
# 1. ZeroDivíionError
# 2.NameError
# 3.TypeError
#  --> phần còn lại sau type: giải thích nguyên nhân cụ thể
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# --> cho biết file nào bị lỗi/ dòng nào bị lỗi
# --------> xảy ra khi đang chạy    
try: 
    x = 10/0
except:
    print('Có lỗi xảy ra')

try:
    x = 10 / 0
    y = int("abc")
except ZeroDivisionError:
    print("Chia cho 0")
except ValueError:
    print("Sai kiểu dữ liệu")
# lấy thông tin lỗi
try:
    x = 10 / 0
except Exception as e:
    print("Lỗi:", e)
# ==============================
# 11.pattern chuẩn
# try:
#     # code
# except SpecificError:
#     # xử lý
# except Exception as e:
#     # fallback
# else:
#     # nếu ok
# finally:
#     # cleanup
# ==================================
# age = int(input("Nhập tuổi:"))
# print("Tuổi", age)
# 

# *************************************
# 8.3: Handling Exceptions (xử lý ngoại lệ)

try:
    age = int(input("Nhập tuổi:"))
    print("Tuỏi:", age)
except ValueError:
    print("Tuổi phẩi nhập số")
# ví dụ
try:
    with open("input.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("Không tìm thấy file")

except Exception as e:
    print("Lỗi khác:", e)

else:
    print("Đọc file thành công")

finally:
    print("Kết thúc chương trình")

# *************************************
# 8.4:Raising Exceptions (Tự phát sinh lỗi)

# cú pháp: raise ExceptionType("message")
# raise ValueError("Giá trị không hợp lệ")

age1 = int(input("Nhập tuổi: "))

if age1 < 0:
    raise ValueError("Tuổi không được âm")

print("Tuổi hợp lệ")
# 11. Tóm tắt cần nhớ
# raise           → tạo lỗi
# raise e         → ném lại lỗi
# raise ... from  → nối lỗi (debug)
# custom class    → tạo lỗi riêng
