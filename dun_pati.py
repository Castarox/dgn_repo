class Stuff():

    def __init__(self, name, weigt, st_type, sign):
        self.name = " "
        self.weight = 0
        self.st_type = " "
        self.sign = " "

onion = Stuff('onion', 10, 'food', 'a')
carrot = Stuff('carrot', 10, 'food', 'b')
hat = Stuff('hat', 10, 'clothes', 'c')
goat = Stuff('goat', 10, 'other', 'd')
knife = Stuff('knife', 10, 'weapons', 'e')


def find_object(what):
    items = ['a','b','c','d','e']
    print("You found %s" % items[what])

    print("masz przedmiot")
