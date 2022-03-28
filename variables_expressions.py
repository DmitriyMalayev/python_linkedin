# Numbers (integers, floating point values),
# Strings(collection of characters),
# Booleans (True or False),
# Sequences (Lists, Tuplles (can't be changed)),
# Dictionaries (map unique keys to specific values)

myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
myturple = (0, 1, 2)
mydict = {"one": 1, "two": 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mydict)

myint = "abc"
print(myint)

# accessing a member of a sequence using index

print(mylist[2])
print(myturple[1])

# Using slice  (start index : end index : step value)
print(mylist[1:5])
print(mylist[1:5:2])
print(mylist[::-1])  # reverse order trick

# Using key returns the value for that key.
print(mydict("one"))

# Variables of different data types can't be combined
print("Hello" + 123)  # TYPE ERROR

print("Hello" + str(123))  # converts to string


# Global vs. Local Variables

def someFunction():
  global mystr #indicating that mystr is already present in the global namespace and to use that
  mystr = "def"  #local variable
  print(mystr)


someFunction() #def
print(mystr) #This is a string  (from global variable) def if global is used 

# deleting a variable 
del mystr 

