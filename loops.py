

def main():
    x = 0
    
    print('Printing with for loop')
    for i in range(1, 10):
        print(i)
    
    print("\n")
    print('Printing with while loop')
    while (x<5):
        print(x)
        x = x + 1
    
    print("\n")
    print('Printing with for loop along with break statement')
    for i in range(1, 10):
        if (i == 5) : break
        print(i)

    print("\n")
    print('Printing with for loop along with continue statement')
    for i in range(1, 10) :
        if (i % 2 == 0) : continue
        print(i)

    print("\n")
    print('Printing with for loop with enumerate')
    for key, value in enumerate(range(1,10)) :
        print(key, value)

if __name__ == '__main__' :
    main()
