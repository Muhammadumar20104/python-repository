# Keyword Arguments
def fun(name='umar' , age=26 , language='English'):
    print(name,age,language)
fun()
fun('abubakar',30,'arabi')
fun(name='junaid')

# Flexible Number of Arguments

def add(*args):
    total=0
    for i in args:
        total += i
    print(total)
a=(3,6,9)
print(a[0])
add(6,9)
    