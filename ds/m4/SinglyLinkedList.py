from Node import Node


def print_node(node):
    current = node.head
    while current:
        print(current.data)
        current = current.next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # # NOTE: time complexity -> O(n) to O(1)
    # def append(self, data):
    #     # encapsulate data in Node
    #     node = Node(data)
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         current = self.head
    #         while current.next:
    #             current = current.next
    #         current.next = node

    # NOTE: improved time complexity from O(n) to O(1) with tail reference
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    # NOTE: update 2 links, point previous node to new node
    # point new node to successor of previous node
    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
                # print(count)
                return
            elif index == index:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("The list has less number of elements")

    def delete_first_node(self):
        current = self.head
        if self.head is None:
            print("No data element to delete")
        elif current == self.head:
            self.head = current.next

    def delete_last_node(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next
                self.size -= 1
            prev = current
            current = current.next

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    # yield used to return from function while saving states of its
    # local variables to enable function to resume from where it left off
    # whenever function is called again, execution starts from the last yield statement
    # any function that contains a yield keyword is termed a generator
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True

        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.tail = None
        self.head = None


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

for word in words.iter():
    print(word)
print()

words.append_at_a_location('new', 2)

for word in words.iter():
    print(word)
print()

print(words.search('sspam'))
print(words.search('spam'))
print()

words.delete_first_node()
for word in words.iter():
    print(word)
print()

words.delete_last_node()
for word in words.iter():
    print(word)
print()

words.delete("ham")
for word in words.iter():
    print(word)
print()
