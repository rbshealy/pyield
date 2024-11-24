from enum import Enum

class HyperBool(Enum):
    TRUE = 1.0
    FALSE = 0.0
    X = 0.5
    ERR = float('inf')

    concrete_vals = [1.0, 0]
    non_concrete_vals = [0.5, float('inf')]

    def __init__(self):
        self.concrete = True

    def __repr__(self):
        return f"HyperBool(value = {self.value})"

    def __add__(self, other):
        if self.__class__ is other.__class__:
            if self.value in self.concrete_vals and other.value in self.concrete_vals:
                return HyperBool(bool(self.value) or bool(other.value))
            else:
                return HyperBool(self.value + other.value)
        return NotImplemented

    def __mul__(self, other):
        if self.__class__ is other.__class__:
            return HyperBool(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if self.__class__ is other.__class__:
            return HyperBool(self.value + other.value)
        return NotImplemented

    def __truediv__(self, other):
        if self.__class__ is other.__class__:
            return HyperBool(self.value + other.value)
        return NotImplemented




