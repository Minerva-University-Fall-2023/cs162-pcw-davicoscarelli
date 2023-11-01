class BlankClass(object):
    '''This is a Blank class for CS162. And it's as empty as my motivation.'''
    pass

t = BlankClass()

class ClassWithAttr(object):
    x1 = 1
    x2 = 2
    x3 = "This attribute is just here to make up numbers."

my_attr = ClassWithAttr()
my_attr.x4 = "Another random attribute. Yay!"

if __name__ == "__main__":
    print(type(t))
    print(dir(t))