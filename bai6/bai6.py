def fib(n):
    a,b =0,1
    while a < n:
        print (a, end=' ')
        a,b = b, a+b+6
    print()

def fib2(n):
    result =[]
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result

if __name__== '__main__':
    import sys
    fib(int(sys.argv[1]))
#     print(fib(6))
#     print(fib2(8))
# -------------------------------
# 6.1.1:chạy modules như script
# lệnh chạy python trực tiếp trong file module
# python bai6.py 10 (gõ trong terminal)
