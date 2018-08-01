

def if_else_statement():
    x ,y = 10, 100

    print("Value of X & Y : " + str(x) + " " + str(y))
    if (x > y):
        print("X is greater than Y")
    else:
        print("Y is greater than X")
        

def if_elif_else_statement():
    x, y = 100, 100
    
    print("Value of X & Y : " + str(x) + " " + str(y))
    if (x > y):
        print("X is greater than Y")
    elif (x == y):
        print("X is same as Y")
    else:
        print("Y is greater than X")

def single_line_if():
    x, y = 100, 10

    print("Value of X & Y : " + str(x) + " " + str(y))
    result = "X is greater than Y" if (x>y) else "Y is greater than or same as X"
    print(result)


if_else_statement()
if_elif_else_statement()
single_line_if()

