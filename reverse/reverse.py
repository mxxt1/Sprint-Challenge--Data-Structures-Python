class Node:
    def __init__(self, value=None, next_node=None):
        # value and next
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if node exists and it's not None assign the next node to a #holding variable and reassign next_node to the prev. Assign #prev to current node and then assign current to holding #variable and pass the reassigned current and prev and recurse #reverse_list. If node doesn't exist or is None then the head #should be prev

        if node and node is not None:
            # assign next to variable
            next = node.next_node
            # set next_node to prev
            node.next_node = prev
            # prev = current node
            prev = node
            # current = current's next node
            node = next
            # call reverse on new current, pass prev
            self.reverse_list(node, prev)
        else:
            # if node false or none then head is prev
            self.head = prev
