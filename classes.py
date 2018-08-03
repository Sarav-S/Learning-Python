

class baseClass():
    def method_one(self):
        print("This is method one from base class")

    def method_two(self, string):
        print("This is second method from base class" + string)

class anotherBaseClass():
    def method_one(self):
        print("This is another method from different class")

class inheritedClass(baseClass, anotherBaseClass):
    def method_one(self):
        baseClass.method_one(self)
        anotherBaseClass.method_one(self)
        print("This is method one from inherited class")

    def method_two(self, string):
        print("This is second method from inherited class")


def main():
    newClass = baseClass()
    newClass.method_one()
    newClass.method_two("Howdy?")

    extractedClass = inheritedClass()
    extractedClass.method_one()
    extractedClass.method_two("Howdy?")


if __name__ == '__main__':
    main()
