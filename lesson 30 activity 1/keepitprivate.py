class myclass:
    __privateVar=15;
    def __privMeth(self):
        print("i'm inside class myclass")
    def hello(self):
        print("private variable value",myclass.__privateVar)
obj= myclass()
obj.hello()
obj.__privMeth()
