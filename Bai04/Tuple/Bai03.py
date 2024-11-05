a = str(input("Hãy nhập list: "))
manglist = a.split(",");
a = str(input("Hãy nhập Tuple: "))
mangtuple = tuple(a.split(","))
xlist = manglist+list(mangtuple)
print("outputList =",list(xlist), end = ", ")
print("outputTuple =",tuple(xlist))