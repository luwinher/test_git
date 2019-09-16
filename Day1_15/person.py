#

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def paly(self):
        print('%s is play a game happily.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s is watch a av.' % self._name)
        else:
            print('%s is watch a katong.' % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s of %s is study %s' % (self._name, self._grade, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s is teach %s.' % (self._name, self._title, course))


def main():
    stu = Student('Wang', 15, 'Sinner 3')
    stu.study('Math')
    stu.watch_av()
    te = Teacher('Luo', 38, 'Teacher')
    te.teach("Python")
    te.watch_av()

if __name__ == '__main__':
    main()







