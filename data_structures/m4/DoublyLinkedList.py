class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def append_at_start(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def append_at_a_location(self, data):
        current = self.head
        prev = self.head
        new_node = Node(data, None, None)
        while current:
            if current.data == data:
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                current.prev = new_node
                self.count += 1
            prev = current
            current = current.next

    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            print("List is empty")
        elif current.data == data:
            self.head.prev = None
            node_deleted = True
            self.head = current.next
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
            if not node_deleted:
                print("Item not found")
        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print(" Data item is present in the list. ")
                return
        print(" Data item is not present in the list. ")
        return


words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

for word in words.iter():
    print(word)
print()

words.append_at_start('book')
for word in words.iter():
    print(word)
print()

words.append('book')
for word in words.iter():
    print(word)
print()

words.append_at_a_location('ham')
for word in words.iter():
    print(word)
print()

words.delete('ham')
for word in words.iter():
    print(word)
print()

words.delete('spam')
for word in words.iter():
    print(word)
print()

words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

words.contains("ham")
words.contains("ham2")
