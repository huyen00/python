# 7.2: Reading and writing file (ĐỌc và ghi tệp tin)
with open('bai5.py', encoding="utf-8") as f: # bai5.py là tên file cần đọc cần viết đúng tên và đuôi 100%
    read_data = f.read()
print("f.closed", f.closed)
print("read_data=", read_data) #sẽ in ra toàn bộ nộ dung trong file bai5.py

# ------------------------------
# 7.2.1: Methods of file objects( các phương thức của đối tượng file)
# "w" → tạo file + ghi đè
# "a" → thêm nội dung
# "r" → đọc file
# with → tự động đóng file
with open("D:/oneportal/Huyen/python/bai7/test.txt", 'w', encoding ='utf-8') as fn: #tạo 1 file mới nếu chưa có, vào đúng đường dẫn 
    fn.write("Hello Python")
with open("D:/oneportal/Huyen/python/bai7/test.txt",'a',encoding='utf-8') as fn: #thêm nội dung vào file
    fn.write('\n Thêm 1 dòng mới vào file')
    fn.write('\n Thêm 1 dòng mới vào file 2')
with open("D:/oneportal/Huyen/python/bai7/test.txt", 'r', encoding='utf-8') as fn: # r: đọc file
    # print("Nội dung file test.txt:", fn.read()) # read(n):đọc n kí tự trong file, nếu không có n sẽ đọc toàn bộ file
    line = fn.readline() # đọc 1 dòng trong file
    print("Đọc 1 dòng trong file test.txt:",line) # nếu bạn dùng 2 câu lệnh đọc file liên tiếp thì câu lệnh thứ 2 sẽ trả về chuỗi rỗng, vì lệnh 1 đã đọc hết file
    fn.seek(0) # đưa con trỏ về đầu file để đọc lại từ đầu
    print("Nội dung file test.txt:", fn.read())
    
    fn.seek(0)
    lines = fn.readlines() # đọc tất cả các dòng trong file và trả về 1 list
    print("Nội dung file test.txt trả về 1 list:", lines) # sẽ in ra 1 list chứa tất cả các dòng trong file
# Duyệt file theo từng dòng
with open("D:/oneportal/Huyen/python/bai7/test.txt", 'r', encoding='utf-8') as fn:
    for i,line in enumerate(fn): # duyệt file theo từng dòng/ enumerate(fn) sẽ trả về cả chỉ số dòng và nội dung dòng
        print("line", i, ":", line) 
with open("D:/oneportal/Huyen/python/bai7/test.txt", 'a+', encoding='utf-8') as fn:
    fn.writelines(["\n Thêm 1 dòng mới vào file 3", "\n Thêm 1 dòng mới vào file 4"]) # thêm nhiều dòng vào file
    print("Nội dung file test.txt sau khi thêm nhiều dòng:", fn.read())
    
with open("D:/oneportal/Huyen/python/bai7/test.txt", 'r+', encoding='utf-8') as fn: #r+: đọc và ghi fille
    print("Đọc nội dung :", fn.read())
    fn.write("\nHelooo")
    fn.seek(0)
    print("Nội dung file test.txt sau khi thêm 1 dòng mới:", fn.read()) # sẽ không in ra nội dung mới vì con trỏ đã ở cuối file, cần dùng fn.seek(0) để đưa con trỏ về đầu file để đọc lại từ đầu
# ==================================
# Mode	Ý nghĩa
# r	đọc text
# r+	đọc + ghi text
# rb	đọc nhị phân
# rb+	đọc + ghi nhị phân
# wb	ghi nhị phân (ghi đè)
# ab	thêm nhị phân
# ==================================
# 7.2.2: Save structured data with json (lưu dữ liệu có cấu trúc với json)
# Hàm	        Ý nghĩa
# json.dump()	ghi Python → file JSON
# json.load()	đọc file JSON → Python
# dumps → Python → string
# loads → string → Python
import json
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Angular"]
}
with open("D:/oneportal/Huyen/python/bai7/data.json", 'r+', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4) # ghi dữ liệu vào file data.json/ ensure_ascii=False để hiển thị tiếng Việt, indent=4 để định dạng file json đẹp hơn
    f.seek(0) # đưa con trỏ về đầu file để đọc lại từ đầu
    data = json.load(f) # đọc file json
    print("json:", data)
x = [1,'simple','list']
test = json.dumps(x) # chuyển list thành string json
print("test=", test)