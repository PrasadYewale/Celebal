class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if self.head is None:
            raise Exception("List is empty. Nothing to delete.")
        if n <= 0:
            raise Exception("Index must be greater than 0.")
        if n == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(n - 2):
            if current.next is None:
                raise Exception("Index out of range.")
            current = current.next
        if current.next is None:
            raise Exception("Index out of range.")
        current.next = current.next.next

# Sample test
ll = LinkedList()
ll.add_node(5)
ll.add_node(15)
ll.add_node(25)
ll.add_node(35)

print("Original List:")
ll.print_list()

print("After deleting 3rd node:")
ll.delete_nth_node(3)
ll.print_list()
