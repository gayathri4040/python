n = eval(input("Enter the limit for the fibonacci series to be printed: "))
first = 0
second = 1
print(first,second,end=" ")
while n-2>0:
    temp = first+second
    print(temp, end = ' ')
    first = second
    second = temp
    n -= 1
#if not this print() line, a '%' will be printed at the end
print()
