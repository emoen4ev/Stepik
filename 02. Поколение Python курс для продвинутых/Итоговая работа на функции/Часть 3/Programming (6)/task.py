def compose(f, g):
    def h(x):
        return f(g(x))
    return h


# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

'''
28
17
3333333
35
'''