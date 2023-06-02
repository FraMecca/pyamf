# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

"""
Python compatibility values and helpers.
"""

try:
    import __builtin__ as builtins
except ImportError:
    import builtins


import types

func_types = (
    types.BuiltinFunctionType, types.BuiltinMethodType, types.CodeType,
    types.FunctionType, types.GeneratorType, types.LambdaType, types.MethodType
)

class_types = (type, )
int_types = (int, )
str_types = (str, bytes)
PosInf = 1e300000
NegInf = -1e300000
# we do this instead of float('nan') because windows throws a wobbler.
NaN = PosInf / PosInf

def isNaN(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NaN)


def isPosInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(PosInf)


def isNegInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NegInf)


def callable(obj):
    """
    Compatibility function for Python 3.x
    """
    from typing import Callable
    return isinstance(obj, Callable) or hasattr(obj, '__call__') # TODO: can remove second cond
