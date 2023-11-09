
def tes1(name,age):
    print(name , age)


# test1('Nick',29)

def test2(*figures):
    for i in figures:
        print(i)

# test2(20,50,90)

# test2(50,90)

def test3(a,b):
    return a+b , a-b

result = test3(50,30)
# print(result)

def test4(name,salary = 9000):
    print('Name:{} Salary:{}'.format(name,salary))

# test4('Ben',12000)
# test4('Jessa')

def test5(a,b):

    def inner(a,b):
        return a+b 

    plus = inner(a,b)
    return plus + 5

# res = test5(5,10)

# print(res)












def test6(num):
    if num:
        return num + test6(num - 1)

    else:
        return 0

# res = test6(10)
# print(res)

def test7(name , age):
    print(name, age)

test7('Emma' , 30)

show_student = test7

# show_student('Emma' , 30)

def test8():
    print(list(range(4,30,2)))
test8()

def test9():
    x = [11,50,63,91,75]
    print(max(x))

test9()