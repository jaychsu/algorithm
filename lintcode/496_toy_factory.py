"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')


class Dog(Toy):
    def talk(self):
        print 'Wow'


class Cat(Toy):
    def talk(self):
        print 'Meow'


class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        if type == 'Dog':
            return Dog()
        if type == 'Cat':
            return Cat()
