from argparse import ArgumentError
from enum import Enum

class HyperBool(Enum):
    TRUE = 1.0
    FALSE = 0.0
    X = 0.5
    ERR = float('inf')

    _concrete_vals = [TRUE, FALSE]
    _non_concrete_vals = [X, ERR]

    def __init__(self, value):
        if value.__class__ is bool:
            self.value = HyperBool.eval(value)
        elif value.__class__ is HyperBool:
            self.value = value.value
        elif value.__class__ is float and HyperBool.is_valid(value):
            self.value = value
        else:
            raise ArgumentError(f"Argument {value} must be a valid HyperBool")


        if value in HyperBool._concrete_vals:
            self.is_concrete = True
        else:
            self.is_concrete = False

    def __repr__(self):
        if self.value == HyperBool.TRUE:
            return 'HyperBool.TRUE'
        elif self.value == HyperBool.FALSE:
            return 'HyperBool.FALSE'
        elif self.value == HyperBool.X:
            return 'HyperBool.X'
        elif self.value == HyperBool.ERR:
            return 'HyperBool.ERR'

        return NotImplementedError

    def __bool__(self):
        return NotImplemented

    def __or__(self, other):
        return NotImplemented

    def __and__(self, other):
        return NotImplemented

    def __not__(self):
        return NotImplemented

    def __add__(self, other):
        if self.__class__ is other.__class__:
            if self.is_concrete and other.is_concrete:
                return HyperBool.eval(bool(self.value) or bool(other.value))
            elif self.is_concrete:
                if other.value == HyperBool.X:
                    if bool(self.value):
                        return HyperBool.TRUE
                    else:
                        return HyperBool.X
                else:
                    return HyperBool.ERR
            elif other.is_concrete:
                if self.value == HyperBool.X:
                    if bool(other.value):
                        return HyperBool.TRUE
                    else:
                        return HyperBool.X
                else:
                    return HyperBool.ERR
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


    @classmethod
    def eval(cls, expression):
        if expression:
            return HyperBool.TRUE
        else:
            return HyperBool.FALSE

    @classmethod
    def is_valid(cls, value) -> bool:
        if (value in HyperBool._concrete_vals or value in HyperBool._non_concrete_vals):
            return True
        else:
            return False





