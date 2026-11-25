"""
Binding within the List Monad

In Haskell, Monads are simple containers, or even 'box-like' datastructures, of which lists are included, which can
respond to certain functions, which are defined in the Monad typeclass. (To put it simply!)

In this kata, you must implement the Bind function for lists, or arrays. In haskell, the function is represented by >>=,
but we'll just call it bind.

Essentially, bind should map the array with the function given, and then flatten it one time. Don't manipulate the
original array; make you function pure: without side-effects, so that no variables are edited whilst the function is
carried out. In dynamically typed languages, you should throw an error if the given function does not return a list.

Here's how it should work:

bind( [1,2,3], lambda a: [a+1] )
=> [2,3,4]

bind( [1,2,3], lambda a: [[a]] )
=> [[1],[2],[3]]

bind( [1,2,3], lambda a: a )
=> # ERROR! The returned value is not a list!
As per usual, the ruby function will be passed a Proc or Lambda. Remember that the function still takes two arguments!
"""


def bind(arr, func):
    mapped = [func(x) for x in arr]
    for item in mapped:
        if not isinstance(item, list):
            raise ValueError('The returned value is not a list!')
    return [item for sublist in mapped for item in sublist]


def bind_v2(lst, func):
    return [y for x in lst for y in func(x)]


assert bind([1, 2, 3], lambda a: [a]) == [1, 2, 3]
assert bind([7, 8, 9], lambda a: [[a]]) == [[7], [8], [9]]
assert bind([3, 4, 5], lambda a: [[a, -a]]) == [[3, -3], [4, -4], [5, -5]]
assert bind([5, 6, 7], lambda a: [str(a)]) == ['5', '6', '7']

assert bind_v2([1, 2, 3], lambda a: [a]) == [1, 2, 3]
assert bind_v2([7, 8, 9], lambda a: [[a]]) == [[7], [8], [9]]
assert bind_v2([3, 4, 5], lambda a: [[a, -a]]) == [[3, -3], [4, -4], [5, -5]]
assert bind_v2([5, 6, 7], lambda a: [str(a)]) == ['5', '6', '7']
