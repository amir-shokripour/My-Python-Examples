class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0

    def get(self, ind):
        if ind >= self.size():
            raise IndexError('Index out of range')
        x = self.head.next
        for i in range(ind):
            x = x.next
        return x

    def insert_after(self, x, data):
        y = Node(data)
        y.prev = x
        y.next = x.next
        x.next.prev = y
        x.next = y
        self.n += 1
        return y

    def delete(self, x):
        if self.is_empty():
            raise Exception('List is empty')
        x.prev.next = x.next
        x.next.prev = x.prev
        self.n -= 1
        return x

    def find(self, val):
        x = self.head.next
        while x != self.head:
            if x.data == val:
                return x
            x = x.next
        return None

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

# Example usage
list = List()  # Create the list
list.insert_after(list.head, "milad")  # head <-> milad
list.insert_after(list.get(0), "Arya")  # head <-> milad <-> Arya
list.insert_after(list.find("Arya").prev, "jabbar")  # head <-> milad <-> jabbar <-> Arya
list.delete(list.find("jabbar"))  # head <-> milad <-> Arya
print("Current size of list is", list.size())  # Should print 2
