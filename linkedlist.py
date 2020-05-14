class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add(self, data: int) -> Node:
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return self.head
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(data)
        current.next = new_node
        return self.head

    def push(self, data: int) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert(self, data, index):
        count = 1
        if self.head is None:
            return "index out of bound"
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current and count != index:
            current = current.next
            count += 1
        if count != index:
            return "index out of bound"
        new_node = Node(data)
        temp = current.next
        current.next = new_node
        new_node.next = temp

    def delete(self, data):
        if self.head is None:
            return "No link list to delete"
        current = self.head
        if self.head.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def reverse(self):
        current = self.head
        prev = None
        while current:
            advance = current.next
            current.next = prev
            prev = current
            current = advance
        self.head = prev

    def reverse_in_k_group(self, head, k):
        current = head
        prev = None
        next = None
        count = 0
        while count < k and current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse_in_k_group(next, k)
        return prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print(None)


if __name__ == '__main__':
    link_list = LinkList()
    link_list.add(4)
    link_list.add(3)
    link_list.add(2)
    link_list.add(1)
    link_list.push(6)
    link_list.push(7)
    link_list.push(8)
    link_list.push(9)
    link_list.push(10)
    link_list.print_list()
    link_list.reverse()
    link_list.print_list()
    link_list.insert(5, 4)
    link_list.print_list()
    link_list.insert(0, 0)
    link_list.print_list()
    link_list.head = link_list.reverse_in_k_group(link_list.head, 3)
    link_list.print_list()



