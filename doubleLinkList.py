import random


class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            self.tail = new_node

    def pop(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    return
            cur = cur.next

    def list_generator(self, number_of_elem, start_par, back_par):
        for i in range(number_of_elem):
            data = random.randint(start_par, back_par)
            self._append(data)

    @staticmethod
    def _binary_counter(data, bit):
        binary_str = "{0:b}".format(data)
        if bit == "1":
            ones = binary_str.count('1')
            print(ones, end=" ")
        elif bit == "0":
            zeros = binary_str.count('0')
            print(zeros, end=" ")
        else:
            raise ValueError

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def thr_list(self, side):
        counter = 0
        if side == "traverse":
            cur = self.head
            while cur:
                self._binary_counter(cur.data, "1")
                cur = cur.next
                counter += 1
            print("\nnumber of elements =", counter)

        elif side == "reverse":
            cur = self.tail
            while cur:
                self._binary_counter(cur.data, "0")
                cur = cur.prev
                counter += 1
            print("\nnumber of elements =", counter)
        else:
            raise ValueError


dd = DoubleLinkedList()
dd.list_generator(10, -10, 10)
dd.print_list()
print("\n\n")

