filename = input("Input the Filename: ")
file = filename.split(".")
#repr method prints the official string representation of an object
print("The extension of the file is: ", repr(file[-1]))
