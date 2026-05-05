# Modules
def fib(n):
    """Write Fibonacci series up to n .""" #docstring (chỉ là mô tả, không ảnh hưởng tới logic)
    a,b = 0,1
    while a<n:
        print(a, end =' ')
        a, b = b, a+b
    print()   
# fib(6)
# a=0, b=1
# a<6: True
# in 0 và dấu ' '
# a = 1, b=1
# lặp 2
# a = 1, b = 1
# a<6:True
# in 1 và dấu ' '
# a,b = b, a+b --> a = 1, b = 1+1=2