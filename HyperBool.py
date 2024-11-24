from enum import Enum

class HyperBool(Enum):
    TRUE = 1.0
    FALSE = 0.0
    X = 0.5
    ERR = float('inf')

    _concrete_vals = [TRUE, FALSE]
    _non_concrete_vals = [X, ERR]

    def __init__(self, value):
        self.value = value
        if value in HyperBool._concrete_vals:
            self.is_concrete = True
        else:
            self.is_concrete = False

    def __repr__(self):
        return f"HyperBool(value = {self.value})"

    def __add__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool(bool(self.value) or bool(other.value))
            else:
                return NotImplemented
        return NotImplemented

    def __mul__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool(bool(self.value) and bool(other.value))
            else:
                return NotImplemented
        return NotImplemented

    def __sub__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool(bool(self.value) and bool(other.value))
            else:
                return NotImplemented
        return NotImplemented

    def __truediv__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool(bool(self.value) and bool(other.value))
            else:
                return NotImplemented
        return NotImplemented

    def __pow__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool(bool(self.value) and bool(other.value))
            else:
                return NotImplemented
        return NotImplemented




