def intro():
    print("Hello World")


def functionWithArguments(args1, args2 = 5):
    return args1 + args2

def cube(arg):
    return arg * arg * arg

def multipleArgs(*args):
    result = 0
    for i in args:
        result = result + i

    return result

intro()
print("Function with optional Parameters " + str(functionWithArguments(5)))
print("Function with arguments " + str(functionWithArguments(5,5)))
print("Cube result for 5 : " + str(cube(5)))
print("Multiple args " + str(multipleArgs(5,5,5)))
    
