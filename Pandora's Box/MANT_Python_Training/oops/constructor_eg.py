class Greeting:
    def __init__(self, name):
        self.name = name
        print (self.name)
    def __del__(self):
        print ("Destructor started")
    def SayHello(self):
        print ("Hello", self.name)
x1 = Greeting("Guido")
x2 = x1
del x1
del x2
