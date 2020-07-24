list = eval(input("Input: list = "))
for number in list:
    if number>0:
        print(number, end=" ")
print()

#to print the sum of all the positive numbers present in the list, just for reference
#print(sum(number for number in list if(number>0)))
