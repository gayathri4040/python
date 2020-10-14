print("hello, this is my first python program!!")
print

if 17 > 10:
    print("learnt if condition syntax!")
print("out of if")

print

# I am a comment

"""
I am a multi line comment
"""

# no need to specify the type of the variable
# variables are dynamically allocated
x = "I am a "
y = "coder"
print(x+y)
print

x = 5
y = 3.7
# supports operator overloading
# only if we have to similar variables, else throws an error
print(x+y)
print

#use of **
print(6**4)
print

#logical operators (in, not in)
a=[1,2,3,4]
print(1 in a)
print(10 not in a)
print(10 in a)
print

#use of quotations in python to denote string literals
word = 'word'
print(word)

sentence = "this is a sentense"
print(sentence)

paragraph = """Hello guys, this is a paragraph, and
i used multiple lines
and this is interesting."""
print(paragraph)
print

# use of python numbers
var1 = 1
var2 = 10
print (var1,var2)
print

# use of python strings
str = 'Hello World!'
print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str[2:-1])
print (str * 2)
print (str + "TEST")
print

#use of python lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list2 = [123, 'john']
print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (list2 * 2)
print (list + list2)
print

mylist = ["C", "C++"]
print (mylist)
l = len(mylist)
print (l)
print (len(mylist))
mylist.append("Java")
print (mylist)
mylist.insert(1,"Python")
print (mylist)
mylist.remove("C++")
print (mylist)
mylist.sort()
print (mylist)
mylist.sort(reverse=True)
print (mylist)
print

# use of python tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple)
print (tuple[0])
print (tuple[1:3])
print (tuple[2:])
print (tinytuple * 2)
print (tuple + tinytuple)
print

mytuple = ("C","C++")
print(mytuple)
print(len(mytuple))
print

# use of python sets
myset = {"C","C++"}
print (myset)
myset.add("Java")
print(myset)
myset.remove("C++")
print(myset)
set = {"Hannah", "Justin", "Hannah"}
print (set)
print

# use of python dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())
print

mydict = {"C":"Easy", "C++":"Moderate", "Java":"Tough"}
print(mydict)
print(len(mydict))
mydict["Python"] = "Cool"
mydict["PHP"] = "Web"
print(mydict)
print(mydict.get("Java"))
mydict.pop("C++")
print(mydict)
del mydict["C"]
print(mydict)
mydict["Python"] = "Very cool"
print(mydict)
mydict.clear()
print(mydict)
del mydict
#print(mydict)
