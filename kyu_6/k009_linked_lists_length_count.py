"""
Linked Lists - Length & Count

Linked Lists - Length & Count

Implement length to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not need to be redefined.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next

    return count


def count(head, data):
    total = 0
    current = head
    while current is not None:
        if current.data == data:
            total += 1
        current = current.next

    return total


def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_one_two_three():
    head = None
    head = push(head, 3)  # Список: 3 -> None
    head = push(head, 2)  # Список: 2 -> 3 -> None
    head = push(head, 1)  # Список: 1 -> 2 -> 3 -> None
    return head


list1 = build_one_two_three()

assert length(None) == 0
assert length(Node(99)) == 1
assert length(list1) == 3

assert count(list1, 1) == 1
assert count(list1, 2) == 1
assert count(list1, 3) == 1
assert count(list1, 99) == 0
assert count(None, 1) == 0
