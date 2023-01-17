# def generator():
#     def hello():
#         print('Hello from function!')
#     return hello
#
#
# func = generator()
# func()
#
# print(input)

def talk(say):
    prt = say('Мир')
    print(prt)


def hello(name):
    return f'Привет {name}.'


def goodbye(name):
    return f'Пока {name}.'


talk(hello)  # Привет Мир.

talk(goodbye)  # Пока Мир.