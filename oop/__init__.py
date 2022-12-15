class Triagle:
    def __init__(self):
        self._length1 = 0
        self._andle1 = 0
        self._length2 = 0
        self._andle2 = 0
        self._length3 = 0
        self._andle3 = 0

    def set_length(self, value1, value2, value3):
        self._length1 = value1
        self._length2 = value2
        self._length3 = value3

    def set_andle(self, value1, value2, value3):
        self._andle1 = value1
        self._andle2 = value2
        self._andle3 = value3

    def get_length1(self):
        return self._length1

    def get_length2(self):
        return self._length2

    def get_length2(self):
        return self._length2

    def get_andle1(self):
        return self._andle1

    def get_andle2(self):
        return self._andle2

    def get_andle3(self):
        return self._andle3

    def Pifogor(self):
        if self._length1 * self._length1 == self._length2 * self._length2 + self._length3 * self._length3:
            print('треугольник является прямоугольным')
        elif self._length2 * self._length2 == self._length1 * self._length1 + self._length3 * self._length3:
            print('треугольник является прямоугольным')
        elif self._length3 * self._length3 == self._length1 * self._length1 + self._length2 * self._length2:
            print('треугольник является прямоугольным')
        else:
            print('треугольник не является прямоугольным')

    def print_lenth(self):
        print(self._length1,'-сторона 1',self._length2,'-сторона 2',self._length3,'-сторона 3')
    def print_andgle(self):
        print(self._andle1,'-угол 1',self._andle2,'-угол 2',self._andle3,'-угол 3')

# ro = Triagle()
# ro.set_length(3, 4, 5)
# print(ro.get_length1())
# ro.print_andle()
