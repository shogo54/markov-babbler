import sys


class Ninja:
    def __init__(self, name, honor):
        '''
        constructors are called __init__. This is just how they do things.
        All methods, including constructors, must have self as the first
        parameter. 'self' is used like 'this' in Java, but it is required
        in Python. You cannot implicitly use self in Python the way you can
        sometimes leave off 'this' in Java.
        '''
        self.name = name
        self.honor = honor

    def __lt__(self, other):
        "override the < operator, which allows sorted() to work"
        return self.honor < other.honor

    def __str__(self):
        "toString() method in Python. Overrides how the built-in str() function works on Ninjas"
        return '{} has {} honor'.format(self.name, self.honor)


def main():
    n1 = Ninja('alicia', 99)
    n2 = Ninja('bob', 100)
    n3 = Ninja('carlos', 105)
    n4 = Ninja('deandre', 90)
    ninjas = [n1, n2, n3, n4]
    # print(n1)
    # join is a great function to combine with map and a list
    print(', '.join(map(str, sorted(ninjas))))


if __name__ == '__main__':
    main()
