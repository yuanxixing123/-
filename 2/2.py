import keyword
import sys
from sys import argv,path
import math
import random


a=c=v=1
x,y,z='asdf',2,5
print(a,c,v,x,y,z)
print(type(a),type(x))

print('----------------------------------------------------')
class A:
    pass
class B(A):     #B是子类，A是父类
    pass
print(type(A),type(B))
print(type(A()),type(B()))#type不会认为子类是父类类型，isinstance则认为子类也是父类类型
print(isinstance(A,A))
print(type(A())==A)
print()

print('----------------------------------------------------')
issubclass(bool,int)
print(True+1)
print(False+1)
print(1 is True,True==1)#bool是int子类，false=0，true=1；但是会返回true或false而不是返回1或0

print('----------------------------------------------------')
a1=2**4
print(a1)
print(4/3)
print(4//3)

print('----------------------------------------------------')
str='12345678'
print(str[4:5])
print(str[-7:5])
#str[0]=2,这步操作是错误的，string类型中的元素不可以替换（可以整个都替换但是不可以只替换其中一个元素），list类型可以

print('----------------------------------------------------')
list1=['abcd',123,2.23,'runoob',7+1j]
list2=[12345,'asdf']
print(type(list1[-1]))
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(list2*2)
print(list1+list2)
str1='i;love;you'
list3=str1.split(";")#字符串变为列表
print(list3)
list3=list3[-1::-1]
print(list3)
str1=' '.join(list3)#列表类型变成字符串
print(str1)

print('----------------------------------------------------')
tuple1=('adf',1,2.12)
tuple1=(12)
print(tuple1)#tuple1[0]=1是错误的，元组tuple和string一样，不能替换一个元素只能替换整个

print('----------------------------------------------------')
sites={"google",'zhihu','baidu'}#这是第一种建立集合方式
a2=set('abcdefac')#会自动去掉重复元素;这是第二种种建立集合的方式
b1=set('abcdabcdez')
# a3=set('fasdf','fasf','ffff')这种建立set方式是错的
print(sites,a2,b1)
if 'zhihu' in sites:
    print("yes")
else:
    print("no")
print(a2-b1)#差集，即a2中有的b1中没有
print(a2|b1)#并集，注意不是“+”，a2和b1中所有元素
print(a2&b1)#交集，
print(a2^b1)#a2，b1中不同时存在的元素

print('----------------------------------------------------')
dict={}
dict["one"]="one表示1"
dict[2]='2就是two'
tinydict={'name':'zyx','age':22,}
print(dict)
print(dict['one'],dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(type(tinydict['age']))

print('----------------------------------------------------')
a3=10#python中都用补码来表示
b3=3
a3/=b3
print(a3)
a4=60
b4=13
print(a4&b4)
print(~a4&b4)
print(~(a4&b4))
list4=[1,2,3,4,5,6,7]
print(1 in list4)
print(10 not in list4)
a5=20
b5=20
print(a5 is b5)
a6='str'
b6='str'
print(a6 is b6)

print('----------------------------------------------------')
a=5.23
b=2
print(int(a))
print(complex(a))
print(complex(a,b))
print(a//b)
a=-2.23
b=3.44
c=-1
print(abs(c))
print(math.ceil(a),math.floor(a))
print(math.exp(1))
print(math.fabs(c))
print(math.log(16,2))
print(math.log10(1000))
print(max(1,2,3,4))
print(min(1,2,3,4))
print(pow(2,5),2**5)
print(math.sqrt(4))
print(math.modf(a))#返回参数的小数和整数部分，并且两个的符号都和参数符号相等
print(round(1.53,1))#返回四舍五入的值，1表示保留到小数点后一位

print('----------------------------------------------------')
print(random.choice(range(101)))
print(random.choice([1,2,3,4,5,6,]))
print(random.choice('i love you'))
print(random.randrange(1,100,3))
print(random.randrange(19))
print(random.random())
random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
list=[1,2,3,4,5,6]
random.shuffle(list)
random.shuffle(list)
print(list)
print(random.uniform(5,10))
print(random.uniform(10,4))
print(math.sin(math.pi/2))

print('----------------------------------------------------')
print('"aka"')
print('\a')
print('a\na')
print('学号\t姓名\t年龄')
print('12\tzyx\t12')
print('hello hello hello\r1')
print('a')
print('a\fworld')

print('----------------------------------------------------')
a='hello'
b='world'
print(a[1])
print(a+b)
print(a*2)
print(b[:3])
if 'a' in a:
    print('""a"" in a')
else:
    print("'a' not in a")
c=19
print("i am %s,i am %d years old"%(a,c))
print('%%')
print('''i am a chinese \t aa
aima''')
name='zyx'
a=f'hello {name}'
print(a)
a=f'{1+2}'
print(a)
w={'name':'zyx','age':12}
a=f'{w["name"],w["age"]}'
print(a)
print(f'{1+1}')

print('----------------------------------------------------')
list=[1,2,3,4,5]
print(list)
list.append(6)
print(list)
del list[5]
print(list)
print(max(list),min(list))
for x in ['adf',332,33]:
    print(x)
print(len(list))
list=[[1,2,34],[1,2]]
print(list[0],list[0][1])

print('----------------------------------------------------')
tuple1=(1)
print(type(tuple1))
tuple1=(1,2,3,4,5,6)
print(type(tuple1))
#元组和列表很相似，但是元组不可以更改元素，只能整个删除
for x in tuple1:
    print(x)
del tuple1


print('----------------------------------------------------')
dict={'name':'zyx','age':27}
print("age为%s"% dict.get('age'))
print("name为%s"%dict.get('sex','ad'))


print('----------------------------------------------------')
set1=set(('s','a',2))
print(type(set1),set1)
set1.add(1)
print(set1)
set1.remove(1)
print(set1)
set1.pop()
print(set1)