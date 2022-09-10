
# Unpacking arguments

def  fun(age , no_student,no_class):
    var=(100+age)+(20*no_student)-(10*no_class)
    print(var)
data=[20,40,5]
fun(data[0],data[1],data[2])
fun(*data)