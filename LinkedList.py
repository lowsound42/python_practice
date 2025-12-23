class Node:
    def __init__(self, value):
        self.value = value
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        # Single node case
        if self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node

        current = self.head
        while current.next and current.next.next:
            current = current.next

        node = current.next
        current.next = None
        self.tail = current
        self.length -= 1
        return node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True

    def pop_first(self):
        if self.head is None:
            return None

        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return popped

    def get(self, index):
        if index >= self.length or index < 0:
            return None

        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def set_value(self, index, value):
        current = self.get(index)

        if current:
            current.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.get(index - 1)

        if prev is not None:
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        if pre is not None:
            temp = pre.next
            if temp is not None:
                pre.next = temp.next
                temp.next = None
                self.length -= 1
                return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        if temp is not None:
            after = temp.next
            before = None

            for _ in range(self.length):
                if temp is not None:
                    after = temp.next
                    temp.next = before
                    before = temp
                    temp = after
