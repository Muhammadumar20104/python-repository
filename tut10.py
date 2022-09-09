# def fun(age):
#     girl=age+2
#     return girl

# print(fun(33))

# Default Values for Arguments

# def gender(sex='Unknown'):
#     if sex=='m':
#         print("Male")
#     elif sex=='f':
#         print("Female")
#     print(sex)
# gender('m')
# gender('f')

# Variable Scope
a=23
def var():
    b=33
    print(a)
    print(b)
def var2():
    print(a)
    # print(b)error
var()