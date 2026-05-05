# 5.1 more on lists: kiểu dữ liệu danh sách
# list.append(value)
# Thêm 1 mục vào cuối danh sách
a = [1,2,3]
a[len(a):]= [0,0]
print(a)
a.append(0)
print(a)
# thêm vào đầu danh sách
a[:0] = [0,0]
print(a)
# thêm vào giữa danh sách
b =[3,4,5]
b[1:1] = [0,0,0]
print(b)
# list.extend(interable):lặp từng phần tử và thêm vào list
x = [ 9,8,7]
x.extend([6,5,4])
print(x)

x.extend("anbv")
print(x)
# list insert(index, value,/):chèn một mục vào một vị trí nhất định
y =[3,4,5]
y.insert(2,0)
print(y)
# list remove(value):loại bỏ phần tử đầu tiên có giá trị được chỉ định
y.remove(0)
print(y)
y.remove(4)
print(y)
# list pop(index=-1):loại bỏ phần tử ở vị trí được chỉ định và trả về nó
z = [1,2,3,4,5]
z.pop(2)
print(" list pop(): z =",z)
# list.clear(): xóa tất cả các phần tử khỏi list
z.clear()
print("list clear(): z =",z)
# list.index(value[, start[,stop]]): dùng để tìm vị trí (index) đầu tiên của 1 giá trị trong list
z = [1,2,3,4,5]
z.index(3)
print("list index(): ",z.index(1, 0, 2))
# list.count(value):trả về số lần xuất hiện 1 giá trị trong list
b = [1,2,3,4,5,2,2]
print("list.count(2):", b.count(2))
# list.sort(*,key=None, reverse=False):Sắp xếp các phần tử của list, reverse = True là giảm dần, reverse = False là tăng dần, key=len là sắp xếp theo độ dài của chuỗi
a = [4,25,31,1]
# a.sort()
# print("a.sort(): ",a)
a.sort(reverse=True)
print("a.sort(reverse=True): ",a)
b = ["Huyền","Nhung","Viet","h"]
b.sort(key=len)
print("b.sort(key=len):", b)
# list.reverse():đảo ngược thứ tự các phần tử trong list
b.reverse()
print("b.reverse():", b)
# list.copy():Trả về 1 bản sao nông của list
c = b.copy()
print("list.copy():", c)
# 5.1.1: Sử dụng list làm stack (ngăn xếp)
stack = [3,4,5]
stack.append(6)
stack.append(7)
print("stack sau khi thêm phần tử: ", stack)
stack.pop()
stack.pop(1)
print("stack sau khi loại bỏ phần tử:", stack)
# 5.1.2: sử dụng list làm queue (hàng đợi)
from collections  import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")

print("queue sau khi thêm phần tử:", queue)
queue.popleft() 
print("queue sau khi loại bỏ phần tử đầu:", queue)
queue.pop()
print("queue sau khi loại bỏ phần tử cuối:", queue)
# 5.1.3: list comprehénions: biêu thức tạo list
squares = []
for x in range(11):
    squares.append(x**2) # thêm bình phương của x vào list squares
print("squares:", squares)
s1 = list(map(lambda x:x**3, range(10)))
print("s1:", s1)
s2 =[]
for x in range(10):
    s2.append((lambda x: x**2)(x))
print("s2:", s2)
vec = [-4,-2,0,2,4]
vec1=[x for x in vec if x>=0]
print("vec1:", vec1)
vec2=[(x,x**2) for x in range(6)]
print("vec2:", vec2) # vec2= [(0,0),(1,1),(2,4),(3,9),(4,16),(5,25)]
# 5.1.4: Nested List Comprehensions: biểu thức tạo list lồng nhau
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
transposed = [[row[i] for row in matrix] for i in range(4)]
print("transposed:", transposed)
# 5.2 the del statement : câu lệnh del (xóa phần tử có vị trí khỏi danh sách )
a = [-1,1,66.25,333,333,1234.5]
del a[1]
print("a sau khi xóa phần tử tại vị trí 1:", a)
del a[0:3]
print("a sau khi xóa phần tử tại vị trí 0 đến 3:", a)
del a[:]
print("a sau khi xóa tất cả phần tử:", a)
# 5.3 Tuples and sequences: kiểu dữ liệu tuple và chuỗi
t = 12345,54321,"hello!"
print("t:", t)
print("t[0]:", t[0])
# Kiểu dữ liệu tuple bao gồm 1 số giá trị được phân tách bởi dấu phẩy,
#  t =(123,11,'hello') cũng là một tuple
# 5.4: Sets: kiểu dữ liệu tập hợp
basket = {"apple","orange","apple","pear","orange","banana"}
print("basket:", basket)
a = set("Huyền")
print("a:", a)
b = set("Nhung")
print("b:", b)
print("a - b:", a - b) # phần tử có trong a nhưng không có trong b
print("a | b:", a | b) # phần tử có trong a hoặc b hoặc cả hai
print("a & b:", a & b) # phần tử có trong cả a và b

a = {x for x in "abracadabra" if x not in 'abc'}
print("a:",a) # x = a,b,r,c,d và not abc nên a ={r,d}
# 5.5: Dictionaries: kiểu dữ liệu từ điển từ các chuỗi cặp khóa - giá trị
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print("tel:", tel) # {'jack': 4098, 'sape': 4139, 'guido': 4127}
del tel['sape']
print("tel sau khi xóa phần tử có key 'sape':", tel) # {'jack': 4098, 'guido': 4127}
tel1= dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("tel1:", tel1)
# 5.6: Looping techniques: kỹ thuật lặp
# khóa và giá trị được truy xuất cùng lúc bằng phương thức .items()
knights = {'gallahad':'the pure', 'robin':'the brave','0s':'1'}
for k,v in knights.items():
    print(k,v)
# chỉ xóa và giá trị tương ứng có thể được truy xuất cùng lúc bằng hàm enumerate()
for i, v  in enumerate(['tic','tac','toe']):
    print(i,v  )
# để lặp qua 2 hoặc nhiều chuỗi cùng lúc, các mục có thể dược ghép nối với hàm zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("q: {}, a: {}".format(q, a))
    print('What is your {0}?  It is {1}.'.format(q, a))
# để lặp qua các phần tử của một danh sách theo thứ tự đã sắp xếp, sử dụng hàm sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# 5.8: comparing sequences and other types
