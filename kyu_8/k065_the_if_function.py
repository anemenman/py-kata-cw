"""
The 'if' function

Create a function that takes three arguments:

a value to be evaluated for truthiness.
a function to execute if the first argument is truthy.
a function to execute if the first argument is falsy.
If the first argument evaluates to truthy, call the second argument (a function). If it evaluates to falsy, call the
third argument instead (also a function).

In statically-typed languages, the first argument will be a boolean. In dynamically-typed languages that attribute a
truth value to all expressions, it may be of any type.
"""
from collections.abc import Callable
from typing import Any


def _if(value: Any, truthy_func: Callable[[], Any], falsy_func: Callable[[], Any]) -> Any:
    if value:
        return truthy_func()
    else:
        return falsy_func()


for falsy in (False, None, 0, 0.0, '', [], (), {}, set(), range(0)):
    def on_truthy():
        return 'T'


    def on_falsy():
        return 'F'


    result = _if(falsy, on_truthy, on_falsy)
    assert result == 'F'

for truly in (True, 1, -1, 0.1, ' ', '0', 'False', [0], (None,), {'a': 1}, object()):
    def on_truthy():
        return 'T'


    def on_falsy():
        return 'F'


    result = _if(truly, on_truthy, on_falsy)
    assert result == 'T'
