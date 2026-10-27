"""
Linked Lists - Remove Duplicates

Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes from
the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        current1 = self
        current2 = other

        while current1 is not None and current2 is not None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next

        return current1 is None and current2 is None


def remove_duplicates(head):
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_list(l):
    head = None
    for data in l:
        head = push(head, data)

    return head


assert remove_duplicates(None) is None
assert remove_duplicates(Node(23)).data == 23
assert remove_duplicates(build_list([1, 2, 2])) == build_list([1, 2])
assert remove_duplicates(build_list([1, 2, 3])) == build_list([1, 2, 3])
assert remove_duplicates(build_list([1, 1, 1, 1, 2, 2, 2, 2])) == build_list([1, 2])
