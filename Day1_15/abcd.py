#

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    #@abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: WangWangWang' % self._nickname)


class Cat(Pet):
    def make_voice(self):
        print('%s: Miao...Miao...Miao' % self._nickname)


class Snake(Pet):
    pass
def main():
    pets = [Dog('WangCai'), Cat('Kitty'), Dog('Big Yellow'), Snake('Snake')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
