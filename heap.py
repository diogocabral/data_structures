import math


class Heap:

    def __init__(self):
        self.elements = []

    def add(self, number):
        self.elements.append(number)
        if len(self.elements) > 1:
            self._verify_if_parent_is_higher(len(self.elements) - 1)

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        return None

    def pool(self):
        if len(self.elements) >= 1:
            element = self.elements[0]
        if len(self.elements) >= 1:
            self.elements[0] = self.elements[len(self.elements) - 1]
            del self.elements[len(self.elements) - 1]
            self._balance(0)
            return element
        else:
            return None

    def _left_child_index(self, index):
        return index * 2 + 1

    def _right_child_index(self, index):
        return index * 2 + 2

    def _parent_index(self, index):
        return int((index - 1)/2)

    def _verify_if_parent_is_higher(self, index):
        if self.elements[self._parent_index(index)] < self.elements[index]:
            self.elements[index], self.elements[self._parent_index(index)] = \
                self.elements[self._parent_index(index)], self.elements[index]
        if self._parent_index(index) > 0:
            self._verify_if_parent_is_higher(self._parent_index(index))

    def _balance(self, index):
        left_child_index = self._left_child_index(index)
        right_child_index = self._right_child_index(index)

        new_index = index
        if len(self.elements) >= left_child_index + 1:
            if self.elements[index] < self.elements[left_child_index]:
                new_index = left_child_index

        if len(self.elements) >= right_child_index + 1:
            if self.elements[index] < self.elements[right_child_index] and \
                    self.elements[right_child_index] > \
                    self.elements[left_child_index]:
                new_index = right_child_index

        if index != new_index:
            self.elements[index], self.elements[new_index] = \
                self.elements[new_index], self.elements[index]
            self._balance(new_index)

    def print_array(self):
        print self.elements

heap = Heap()

heap.add(13)
heap.print_array()
heap.add(20)
heap.print_array()
heap.add(9)
heap.print_array()
heap.add(7)
heap.print_array()
heap.add(8)
heap.print_array()
heap.add(5)
heap.print_array()
heap.add(6)
heap.print_array()
heap.add(1)
heap.print_array()
heap.add(1)
heap.print_array()
heap.add(3)
heap.print_array()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
print heap.pool()
