class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        return "index 번째 노드를 반환해보세요!"

    def add_node(self, index, value):
        new_node = Node(value)
        node = self.get_node(index)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return

    def delete_node(self, index):
        if index == 0:
           self.head = self.head.next
           return
        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()