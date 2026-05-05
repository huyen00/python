def ask_ok (prompt, retries = 4, reminder = 'Please try again!'):
    while True:
        reply = input (prompt)
        if reply in {'y', 'ye','yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('Bạn hãy nhập yes hoặc no: ',8,'Dừng lại!!!!')
# giá trị mặc định chỉ được đánh giá 1 lần và  được đánh giá tại thời điểm định nghĩa hàm trong phạm vi định nghĩa
i = 5
def f(arg = i):
    print("arg = ", arg)
i = 6
# f()
# hàm sau sẽ tích lũy các đối số được truyền cho nó trong các lần gọi tiếp theo
def f(a,L=[]):
    L.append(a)
    return L
# print(f(5))
# print(f(10))
# print(f(15))
# Nếu bạn không muốn giá trị mặc định được chia sẻ giữa các lần gọi tiếp theo, bạn có thể viết hàm như sau
def f(a, L=None):
    if L is None:
        L =[]
    L.append(a)
    return L
# print(f(5, [6,7]))
# print(f(10,[0]))
# 4.9.2 Các hàm có thể được gọi bằng cách sử dụng các đối số từ khóa có djang kwarg = value
def parrot (voltage, state = 'a stiff', action ='voom', type = 'Norwegian Blue'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# parrot(1000.0,action ="delete" ) # 1 positional argument
# 4.9.3 Tham số chỉ định vị trí
# vi dụ hàm truyền đối số bất kì
# Có thể truyền bất kì đối số chỉ vị trí hoặc đối số từ khóa
def standard_arg(arg):
    print(arg)
# standard_arg(2) 
# hàm bắt buộc phải truyền đối số chỉ vị trí vì có dấu / ở cuối tham số
def pos_only_arg(arg, /):
    print(arg)
# pos_only_arg(1)
# hàm bắt buộc phải truyền đối số từ khóa vì có dấu * ở đầu tham số
def kwd_only_arg(*, arg):
    print(arg)
# kwd_only_arg(arg =1)
  
# 4.9.4 Lits
def concat(*args, sep="...."):
    return sep.join(args)
# print(concat("earth","mars","venus"))
# 4.9.5 Unpacking argument lists: giaỉ nén danh sách đối số
print(list(range(3,7)))
arg = [3,7]
print(list(range(*arg)))
# 4.9.6: lambda expressions: biểu thức lambda
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(10))
# 4.9.7: documentation strings: chuỗi tài liệu




