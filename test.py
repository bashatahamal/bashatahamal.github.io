# def foo(x, a, b, i, j):
#     k = j
#     ct = 0
#     while k > i-1:
#         # print(k, x[k])
#         if x[k] <= b and not (x[k] <= a):
#             ct = ct + 1
#         k = k - 1
#     return ct

# x = [11,10,10,5,10,15,20,10,7,11]
# print(foo(x,8,18,3,6)) # output 1
# print(foo(x,10,20,0,9)) # output 4
# print(foo(x,8,18,6,3)) # output 0
# print(foo(x,20,10,0,9)) # output 0
# print(foo(x,6,7,8,8)) # output 1


def g(str):
    i = 0
    new_str = ""
    while i < len(str) - 1:
        new_str = new_str + str[i + 1]
        i = i + 1
    return new_str

def f(str):
    if len(str) == 0:
        return ""
    elif len(str) == 1:
        return str
    else:
        return f(g(str)) + str[0]

numstep = 0
def h(n, str):
    while n != 1:
        # print(n, f(str))
        global numstep
        numstep += 1
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        str = f(str)
    return str

def pow(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y-1)

# print(h(1, "fruits"))
# print(h(2, "fruits"))
# print(h(5, "fruits"))
# print(h(pow(2, 1000000000000000), "fruits"))
# print(h(pow(2, 9831050005000007), "fruits"))
print(f'{h(1, "fruits")}{h(2, "fruits")}{h(5, "fruits")}{h(10, "fruits")}{h(100, "fruits")}')

# print(h(10000, "fruits"))
# print(numstep)
# print(h(2, 'fruits'))
# pow(2,5)


