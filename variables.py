# Integer
a = 5
print(a)

# String
name = "Sarav"
print(name)

# Typecasting
print("My name is " + name + ". And I'm " + str(a) + " years old developer")

# Local Variable
def localFunc():
    a = 10
    print(a)

localFunc()
print("Using local variable : " + str(a))

# Global Variable
def globalFunc():
    global a
    a = 10
    print(a)

globalFunc()
print("Using global variable : " + str(a))


