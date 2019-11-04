def convert(x):
    return x/1024
a = 10000
b = (convert(a))
print (str(a) + " b" + " = " + str(b) + " kb")
c = (convert(b))
print (str(a) + " b" + " = " + str(c) + " mb")
