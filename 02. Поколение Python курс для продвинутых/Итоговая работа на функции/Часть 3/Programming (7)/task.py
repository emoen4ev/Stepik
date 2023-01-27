def arithmetic_operation(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '-':
        return lambda x, y: x - y
    elif op == '*':
        return lambda x, y: x * y
    elif op == '/':
        return lambda x, y: x / y

# ---------------------------------------------------

# def arithmetic_operation(op):
#     def operation(x, y):
#         if op == '+':
#             return x + y
#         elif op == '-':
#             return x - y
#         elif op == '*':
#             return x * y
#         elif op == '/':
#             return x / y
#     return operation


# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
#
# print(add(10, 20))
# print(div(20, 5))

'''
30
4.0
'''