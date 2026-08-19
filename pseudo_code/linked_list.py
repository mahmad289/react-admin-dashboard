# Pseudo code for a Singly Linked List in Python
#
# This file contains pseudo code (not runnable) that describes the structure
# and operations of a singly linked list implementation in Python.


# CLASS Node
#     ATTRIBUTES:
#         data       # value stored in the node
#         next       # reference/pointer to the next node (initially None)
#
#     FUNCTION __init__(data):
#         SET self.data = data
#         SET self.next = None


# CLASS LinkedList
#     ATTRIBUTES:
#         head       # reference to the first node in the list (initially None)
#
#     FUNCTION __init__():
#         SET self.head = None
#
#     FUNCTION is_empty():
#         RETURN self.head IS None
#
#     FUNCTION append(data):
#         CREATE new_node WITH data
#         IF self.head IS None:
#             SET self.head = new_node
#             RETURN
#         SET current = self.head
#         WHILE current.next IS NOT None:
#             SET current = current.next
#         SET current.next = new_node
#
#     FUNCTION prepend(data):
#         CREATE new_node WITH data
#         SET new_node.next = self.head
#         SET self.head = new_node
#
#     FUNCTION insert_after(target_data, data):
#         SET current = self.head
#         WHILE current IS NOT None:
#             IF current.data == target_data:
#                 CREATE new_node WITH data
#                 SET new_node.next = current.next
#                 SET current.next = new_node
#                 RETURN True
#             SET current = current.next
#         RETURN False   # target not found
#
#     FUNCTION delete(data):
#         IF self.head IS None:
#             RETURN False
#         IF self.head.data == data:
#             SET self.head = self.head.next
#             RETURN True
#         SET current = self.head
#         WHILE current.next IS NOT None:
#             IF current.next.data == data:
#                 SET current.next = current.next.next
#                 RETURN True
#             SET current = current.next
#         RETURN False   # value not found
#
#     FUNCTION search(data):
#         SET current = self.head
#         SET index = 0
#         WHILE current IS NOT None:
#             IF current.data == data:
#                 RETURN index
#             SET current = current.next
#             INCREMENT index
#         RETURN -1      # not found
#
#     FUNCTION length():
#         SET count = 0
#         SET current = self.head
#         WHILE current IS NOT None:
#             INCREMENT count
#             SET current = current.next
#         RETURN count
#
#     FUNCTION reverse():
#         SET prev = None
#         SET current = self.head
#         WHILE current IS NOT None:
#             SET next_node = current.next
#             SET current.next = prev
#             SET prev = current
#             SET current = next_node
#         SET self.head = prev
#
#     FUNCTION print_list():
#         SET current = self.head
#         WHILE current IS NOT None:
#             PRINT current.data, " -> "
#             SET current = current.next
#         PRINT "None"


# EXAMPLE USAGE (pseudo code):
#     CREATE ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.prepend(5)
#     ll.insert_after(10, 15)
#     ll.print_list()        # 5 -> 10 -> 15 -> 20 -> None
#     ll.delete(15)
#     PRINT ll.search(20)    # 2
#     ll.reverse()
#     ll.print_list()        # 20 -> 10 -> 5 -> None
