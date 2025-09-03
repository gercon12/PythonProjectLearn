'''
class Father():
    def gardening(self):
        print("I enjoy gardening")
class Mother():
    def cooking(self):
        print("I enjoy cooking")
class Children(Father, Mother):
    def sports(self):
        print("I enjoy sports")

c = Children()
c.gardening()
c.cooking()
c.sports()
'''

class Father_1():
    def skills(self):
        print("gardening, programming")
class Mother_1():
    def skills(self):
        print("cooking, art")
class Children_1(Father_1, Mother_1):
    def skills(self):
        Father_1.skills(self)
        Mother_1.skills(self)
        print("sports")

c_1 = Children_1()
c_1.skills()