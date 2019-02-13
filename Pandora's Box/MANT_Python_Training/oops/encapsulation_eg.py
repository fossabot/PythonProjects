class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c
x = Encapsulation(11,13,17)
x.public
x._protected
x._protected = 23
x._protected
x.__private

#wrapping up everything in a single code and for safety purpose.