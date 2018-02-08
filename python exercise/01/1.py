a = 1234
print(a)
a = 'abcd'
print(a)
#可以随意变类型

try:
    print(b)
    #要先定义，不会像C或Java那样默认值为0
except Exception as e:
    print(e)


a = [1,2,3,4]

def func(a):
    a[0] = 2

func(a)
print(a)
#python通过引用传递变量
    
    
