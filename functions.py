# def func1():
#     print("I am a function")


# func1()  # I am a function
# print(func1())  # I am a function.    None.  (because no return value)
# print(func1)  # <function func1 at 0x0000>


def func2(arg1, arg2):
    print(arg1, "", arg2)


def cube(x):
    return x * x * x


# func2(10, 20)
# print(func2(10, 20))
# print(cube(3))

# 10  20
# 10  20
# None
# 27


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# print(power(2))
# print(power(2, 3))
# print(power(x=3, num=2))

# 2
# 8
# 8




def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result

print(multi_add(4,5,10,4,10))  

#33