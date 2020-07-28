def mostFrequent(string):
    map = {}
    for char in string:
        if char not in map:
            map[char] = 1;
        else:
            map[char] += 1;

    #sorting the dictionary by values
    #sorted functions takes three arguments - sorted(iterable list, key, reverse)
    #key -  a function that serves as the basis of sort comparision
    #reverse - in decreasing order
    sortedDict = dict(sorted(map.items(), key = lambda x:x[1], reverse = True))
    for key, value in sortedDict.items():
        print(key,"=",value)

string = input("Enter a string: ")
mostFrequent(string)


"""

1. other way to iterate
for key in sortedDict.keys():
    print(key,"=",sortedDict[key])

2. other way to iterate
sorted_d=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))

"""
