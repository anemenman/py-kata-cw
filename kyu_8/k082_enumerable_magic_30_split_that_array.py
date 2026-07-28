"""
Enumerable Magic #30 - Split that Array!

Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all
the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

animals = ["cat", "dog", "duck", "cow", "donkey"]
partition(animals){|animal| animal.size == 3}
    #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
"""


def partition(lst, predicate):
    true_list = []
    false_list = []

    for item in lst:
        if predicate(item):
            true_list.append(item)
        else:
            false_list.append(item)

    return true_list, false_list


assert partition(["cat", "dog", "duck", "cow", "donkey"], lambda x: len(x) == 3) == (['cat', 'dog', 'cow'],
                                                                                     ['duck', 'donkey'])
