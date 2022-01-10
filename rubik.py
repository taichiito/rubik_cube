from copy import deepcopy
from random import randrange
import sys


class Cube:
    """
        --- --- --- | u00 u01 u02 | --- --- --- | --- --- ---
        --- --- --- | u10 u11 u12 | --- --- --- | --- --- ---
        --- --- --- | u20 u21 u22 | --- --- --- | --- --- ---
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        l00 l01 l02 | f00 f01 f02 | r00 r01 r02 | b00 b01 b02
        l10 l11 l12 | f10 f11 f12 | r10 r11 r12 | b10 b11 b12
        l20 l21 l22 | f20 f21 f22 | r20 r21 r22 | b20 b21 b22
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        --- --- --- | d00 d01 d02 | --- --- --- | --- --- ---
        --- --- --- | d10 d11 d12 | --- --- --- | --- --- ---
        --- --- --- | d20 d21 d22 | --- --- --- | --- --- ---
    """

    def __init__(self):
        self.u = [['w'] * 3 for _ in range(3)]
        self.f = [['g'] * 3 for _ in range(3)]
        self.r = [['r'] * 3 for _ in range(3)]
        self.b = [['b'] * 3 for _ in range(3)]
        self.l = [['o'] * 3 for _ in range(3)]
        self.d = [['y'] * 3 for _ in range(3)]

    @staticmethod
    def rotate_face(face, time=1, copy=True):
        if copy:
            face = deepcopy(face)
        _face = [
            [face[2][0], face[1][0], face[0][0]],
            [face[2][1], face[1][1], face[0][1]],
            [face[2][2], face[1][2], face[0][2]]]
        if time == 1:
            return _face
        else:
            return Cube.rotate_face(_face, time - 1, False)

    @staticmethod
    def rotate_face_inverse(face, copy=True):
        return Cube.rotate_face(face, 3, copy)

    def show(self, face='f'):
        _face = getattr(self, face)
        print('\n'.join([''.join(row) for row in _face]))
        print('---')

    def turn_right(self):
        """
        --- --- --- | u02 u12 u22 | --- --- --- | --- --- ---
        --- --- --- | u01 u11 u21 | --- --- --- | --- --- ---
        --- --- --- | u00 u10 u20 | --- --- --- | --- --- ---
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        b00 b01 b02 | l00 l01 l02 | f00 f01 f02 | r00 r01 r02
        b10 b11 b12 | l10 l11 l12 | f10 f11 f12 | r10 r11 r12
        b20 b21 b22 | l20 l21 l22 | f20 f21 f22 | r20 r21 r22
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        --- --- --- | d20 d10 d00 | --- --- --- | --- --- ---
        --- --- --- | d21 d11 d01 | --- --- --- | --- --- ---
        --- --- --- | d22 d12 d02 | --- --- --- | --- --- ---
        """
        _f = deepcopy(self.f)
        self.f = self.l
        self.l = self.b
        self.b = self.r
        self.r = _f
        self.u = Cube.rotate_face_inverse(self.u)
        self.d = Cube.rotate_face(self.d)

    def turn_left(self):
        self.turn_right()
        self.turn_right()
        self.turn_right()

    def turn_up(self):
        """
        --- --- --- | f00 f01 f02 | --- --- --- | --- --- ---
        --- --- --- | f10 f11 f12 | --- --- --- | --- --- ---
        --- --- --- | f20 f21 f22 | --- --- --- | --- --- ---
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        l02 l12 l22 | d00 d01 d02 | r20 r10 r00 | u22 u21 u20
        l01 l11 l21 | d10 d11 d12 | r21 r11 r01 | u12 u11 u10
        l00 l10 l20 | d20 d21 d22 | r22 r12 r02 | u02 u01 u00
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        --- --- --- | b22 b21 b20 | --- --- --- | --- --- ---
        --- --- --- | b12 b11 b10 | --- --- --- | --- --- ---
        --- --- --- | b02 b01 b00 | --- --- --- | --- --- ---
        """
        _f = deepcopy(self.f)
        self.f = self.d
        self.d = Cube.rotate_face(self.b, 2, False)
        self.b = Cube.rotate_face(self.u, 2, False)
        self.u = _f
        self.r = Cube.rotate_face(self.r)
        self.l = Cube.rotate_face_inverse(self.l)

    def turn_down(self):
        self.turn_up()
        self.turn_up()
        self.turn_up()

    def rotate(self):
        """
        --- --- --- | u00 u01 u02 | --- --- --- | --- --- ---
        --- --- --- | u10 u11 u12 | --- --- --- | --- --- ---
        --- --- --- | l22 l12 l02 | --- --- --- | --- --- ---
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        l00 l01 d00 | f20 f10 f00 | u20 r01 r02 | b00 b01 b02
        l10 l11 d01 | f21 f11 f01 | u21 r11 r12 | b10 b11 b12
        l20 l21 d02 | f22 f12 f02 | u22 r21 r22 | b20 b21 b22
        --- --- --- - --- --- --- - --- --- --- - --- --- ---
        --- --- --- | r20 r10 r00 | --- --- --- | --- --- ---
        --- --- --- | d10 d11 d12 | --- --- --- | --- --- ---
        --- --- --- | d20 d21 d22 | --- --- --- | --- --- ---
        """
        _u = deepcopy(self.u)
        _r = deepcopy(self.r)
        _d = deepcopy(self.d)
        _l = deepcopy(self.l)
        self.f = Cube.rotate_face(self.f)
        self.u[2] = [_l[2][2], _l[1][2], _l[0][2]]
        self.r = [
            [_u[2][0], _r[0][1], _r[0][2]],
            [_u[2][1], _r[1][1], _r[1][2]],
            [_u[2][2], _r[2][1], _r[2][2]]
        ]
        self.d[0] = [_r[2][0], _r[1][0], _r[0][0]]
        self.l = [
            [_l[0][0], _l[0][1], _d[0][0]],
            [_l[1][0], _l[1][1], _d[0][1]],
            [_l[2][0], _l[2][1], _d[0][2]]
        ]

    def rotate_inverse(self):
        self.rotate()
        self.rotate()
        self.rotate()

    def _rotate(self, face, inverse=False):
        self._turn_inverse(face)
        if inverse:
            self.rotate_inverse()
        else:
            self.rotate()
        self._turn(face)

    def _turn(self, face):
        if face in ('u', 'up'):
            self.turn_up()
        elif face in ('r', 'right'):
            self.turn_right()
        elif face in ('l', 'left'):
            self.turn_left()
        elif face in ('d', 'down'):
            self.turn_down()
        elif face in ('b', 'back'):
            self.turn_right()
            self.turn_right()

    def _turn_inverse(self, face):
        if face in ('u', 'up'):
            self.turn_down()
        elif face in ('r', 'right'):
            self.turn_left()
        elif face in ('l', 'left'):
            self.turn_right()
        elif face in ('d', 'down'):
            self.turn_up()
        elif face in ('b', 'back'):
            self.turn_right()
            self.turn_right()

    def rotate_front(self):
        self._rotate('f', False)

    def rotate_front_inverse(self):
        self._rotate('f', True)

    def rotate_up(self):
        self._rotate('u', False)

    def rotate_up_inverse(self):
        self._rotate('u', True)

    def rotate_right(self):
        self._rotate('r', False)

    def rotate_right_inverse(self):
        self._rotate('r', True)

    def rotate_left(self):
        self._rotate('l', False)

    def rotate_left_inverse(self):
        self._rotate('l', True)

    def rotate_down(self):
        self._rotate('d', False)

    def rotate_down_inverse(self):
        self._rotate('d', True)

    def rotate_back(self):
        self._rotate('b', False)

    def rotate_back_inverse(self):
        self._rotate('b', True)


def scramble(n):
    cube = Cube()
    cube.show()

    operations = []

    for _ in range(n):
        operation = randrange(12)
        if operation == 0:
            operations.append('F')
            cube.rotate_front()
        elif operation == 1:
            operations.append("F'")
            cube.rotate_front_inverse()
        if operation == 2:
            operations.append('U')
            cube.rotate_up()
        elif operation == 3:
            operations.append("U'")
            cube.rotate_up_inverse()
        if operation == 4:
            operations.append('R')
            cube.rotate_right()
        elif operation == 5:
            operations.append("R'")
            cube.rotate_right_inverse()
        if operation == 6:
            operations.append('L')
            cube.rotate_left()
        elif operation == 7:
            operations.append("L'")
            cube.rotate_left_inverse()
        if operation == 8:
            operations.append('B')
            cube.rotate_back()
        elif operation == 9:
            operations.append("B'")
            cube.rotate_back_inverse()
        if operation == 10:
            operations.append('D')
            cube.rotate_down()
        elif operation == 11:
            operations.append("D'")
            cube.rotate_down_inverse()
        cube.show()

    print(operations)

    return cube


if __name__ == '__main__':
    scramble(int(sys.argv[1]))
