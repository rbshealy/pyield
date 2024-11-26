from enum import Enum
from random import randrange


class HyperBool(Enum):
    TRUE = 1.0
    FALSE = 0.0
    X = 0.5
    ERR = float('inf')

    _concrete_vals = [TRUE, FALSE]
    _non_concrete_vals = [X, ERR]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def __str__(self):
        return self.name

    def __bool__(self):
        if self.value == HyperBool.TRUE:
            return True
        elif self.value == HyperBool.FALSE:
            return False
        elif self.value == HyperBool.X:
            return randrange(0,2)
        elif self.value == HyperBool.ERR:
            raise ValueError("cannot evaluate HyperBool.Err as a boolean value")

    def __or__(self, other):
        return NotImplemented

    def __and__(self, other):
        return NotImplemented

    def __not__(self):
        return NotImplemented

    def __add__(self, other):
        self_concrete = self.value in HyperBool._concrete_vals
        other_concrete = other.value in HyperBool._concrete_vals

        if self.__class__ is other.__class__:
            if self_concrete and other_concrete:
                return HyperBool.eval(bool(self.value) or bool(other.value))
            elif self_concrete:
                if other.value == HyperBool.X:
                    if bool(self.value):
                        return HyperBool.TRUE
                    else:
                        return HyperBool.X
                else:
                    return HyperBool.ERR
            elif other_concrete:
                if self.value == HyperBool.X:
                    if bool(other.value):
                        return HyperBool.TRUE
                    else:
                        return HyperBool.X
                else:
                    return HyperBool.ERR
            else:
                if self.value == HyperBool.ERR or other.value == HyperBool.ERR:
                    return HyperBool.ERR
                else:
                    return HyperBool.X
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


    @staticmethod
    def eval(expression):
        if expression.__class__ is bool:
            if expression:
                return HyperBool.TRUE
            else:
                return HyperBool.FALSE
        if expression.__class__ is float and HyperBool.is_valid(expression):
            return expression

    @staticmethod
    def is_valid(value) -> bool:
        if value in {HyperBool.TRUE, HyperBool.FALSE, HyperBool.X, HyperBool.ERR}:
            return True
        else:
            return False

    @staticmethod
    def print_table(left, op, right):
        return NotImplemented