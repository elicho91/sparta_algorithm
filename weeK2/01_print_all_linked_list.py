#[3] -> [4]
#data.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



node = Node(3)
first_node = Node(4)
node.next = first_node

# 링크드리스트 생성
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print("cur is ", cur.data)
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



Linked_List = LinkedList(3)

Linked_List.append(4)
Linked_List.append(5)
Linked_List.append(6)
Linked_List.print_all()