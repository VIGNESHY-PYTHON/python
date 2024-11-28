'''
a=2
b="world"
print(a*b)

year=int(input('enter your year'))

if year %4==0 and year %100 !=a or year %400==0:
    print("leap year")
    
else:
    print("not leap year")



text='python'
empty=""
for i in text:

    empty=i+empty
print(empty)
'''
'''
def __init__(self,number):
         self.number=number
         my_str=str(number)
         self.count_values=len(my_str)
          total=0
         for i in my_str:
           total+=int(i) ** count_values
           return number == total 
    
         if number == total:

'''
'''

def amstrang():
    number=int(input("enter your numbers"))
    str_num=str(number)
    len_num=len(str_num)
    tottal=0
    for i in str_num:
        tottal+=int(i) ** len_num
        

    if tottal==number:
        print('its amostrang Number')
    else:
        print("its Not Amstrong Number")
amstrang()

'''
'''
#bitwise

#&, | , ^, ~,<<,>>

a=2&8
print(a)

b=2>>4

print(b)

#string methode

g="python is the programing lag "

print(g.capitalize())


j="python"
print(j[-1:-7:-1])
'''
'''
l=[1,2,3,44,5]
l.append(2)
print(l)

l.extend([1,2,3,4])
print(l)

l.insert(0,10)
print(l)

l.pop(0)
print(l)

l.remove(44)
print(l)

print(l.sort(reverse=True))
print(l)

l1=l.copy()
print(l1)

l2=[2,3,4,5,6,7]

l3=l2.index(5)
print(l3)

l4=[n**2 for n in l2]
print(l4)
'''
'''
s={1,2,3,4,5,5}
b={1,2,3,4,55,5}
s.add('2')
print(s)

s1=s.copy()
print(s1)


s.remove(1)
print(s)
print(s.union(b))

print(s.intersection(b))

A = {1, 2, 3,1}
print()
B = {2,3,1,4}
print(A.isdisjoint(B))

print(A.issubset(B))


n={1,2,3,4,45}
if 1 in n:
    print('yes')


l=[1,2,3,2,1,1,3,4,5]
print(l.count(1))
print(l)

'''
'''
a=(1,2,3)
b=(1,2,3,4)
c=a+b
print(c)


d={'name':'vicky','age':20,'city':'chennai'}
print(d.items())
#insert
d['age2']=21
print(d)
d.setdefault('age3',23)
print(d)

d.update({'name':'vijay'})
print(d)

print(d.get('name'))

#swap to variable

a=10
b=20
temp=a
a=b
b=temp
print('a=',a)
print('b=',b)


c=10
d=20

c=c+d
d=c-d
c=c-d
print(c)
print(d)
'''
#iter

l=[1,2,3,4,5]
x=iter(l)
print(next(x))
print(next(x))

#a=open('filee.txt','x')
a=open('filee.txt','w')
a.write('hello world')
a.close

a=open('filee.txt','a')
a.write(' vicky')
a.close

with open ('filee.txt','r') as f :
    print(f.read())



n=['file.txt','filee.txt']
read_file=lambda n1: open(i,'r') .read()
for i in n:
    print(read_file(i))



from collections import deque
d=deque([1,2,3,4,5,6])
d.appendleft(5)
print(d)

from collections import ChainMap
p={1,2,3,45}
s={1,2,3,445}
chain_map=ChainMap(p,s)
print(chain_map)



from collections import Counter
l=[1,2,3,45]
print(Counter(l))