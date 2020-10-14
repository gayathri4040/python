"""
print(range(2,10))
import random
print(range(2,20,2))
print(range(2,6,10))
print(random.randrange(2,10,2))

list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ", list)
random.shuffle(list)
print ("Reshuffled list : ", list)

str = "hello there"
print(str.find("there"))
s = "this is an example"
print(s.find("exam"))
print(s.find("exam",1111))
print(str.title())
print(s.title())
print(s)
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
##because of white spaces
ss = "hello"
print(ss.isalpha())
print(ss.isdigit())
print(ss.isalnum())
sss = "hello123"
print(sss.isalpha())
print(sss.isdigit())
print(sss.isalnum())
sd = "22222"
print(sd.isalpha())
print(sd.isdigit())
print(sd.isalnum())


str = "...**.hello world..**.."
#str = str[:6] + "python"
print(str)
print("o" in str)
print("o" not in str)
print("x" in str)
print(str.center(40,'.'))
print(str.count('l'))
print(str.count('l',0,3))
print(str.endswith("llo",0,5))
print(str.find("lele"))
#print(str.index("lele")) -> throws error if not found
print(str.isspace())

s = "-"
seq = ("a","b","c")
print(s.join(seq))

print(str.strip("."))
print(str.ljust(15,'.'))
print(str.lstrip('.'))

str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 1))

str = '''this is
string example....
wow!!!'''
print (str.splitlines())


strr = "hello"
tuple1=tuple(strr)
print(tuple1)

dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
string = str(dict)
print (string)
print (string[0:]+"hey there ")
print (type(string))
print (type(dict))
print (type(list))


seq = ('name', 'age', 'sex')
mydict = dict.fromkeys(seq)
print ("New Dictionary : %s" % str(mydict))
dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" % str(dict))

dict = {'Name': 'Zara', 'Age': 7}
list = dict.items()
print (list[0:])
print

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("updated dict : ", dict) """
"""
string = "5+2"
print(string)
print(eval(string))

x,y = eval("10,20+222")
print(x,y)
print(8%007)

a = input("Enter the expression which contains x = ")
x = int(input("enter a number - "))
c = eval(a)
print(c)
print(type(a))
print(type(x))"""
"""
a = input("normal input - ")
print(type(a))
b = eval(input("eval input - "))
print(type(b))"""

def changeme(mylist, list):
    mylist[2] = 111
    list=[10,20,30,40] #adds new reference
    print("inside func - mylist:", mylist)
    print("inside func - list:", list)
    return

mylist = [1,2,3,4]
list = [11,22,33,44]
print("initial mylist:", mylist)
print("initial list:", list)
changeme(mylist, list)
print("after calling func - mylist:", mylist)
print("after calling func - list:", list)
