class Human:
#Properties
    def __init__(self,n, o):
        self.name = n
        self.occupation = o
#Methods
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")
    def speaks(self):
        print(self.name,"says how are you")

#Instance of class / Object
tom =Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

mi_lista = []
