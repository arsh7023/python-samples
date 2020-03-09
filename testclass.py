class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        #print("hello world")

d = Dog('Fido')
d.add_trick('roll over')
print(d.tricks)

