# -*- coding: utf-8 -*-
"""그리고 하나가 남았다
"""
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None
        self.cur = None
        self.before = None
        self.num_of_data = 0

    def insert(self, data):
        self.f_insert(data)

    def f_insert(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.num_of_data += 1

    def insert_front(self, data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.num_of_data += 1

    def l_first(self):
        if self.tail is None:
            return None
        self.before = self.tail
        self.cur = self.tail.next

        return self.cur.element

    def next_node(self):
        if self.tail is None:
            return None
        self.before = self.cur
        self.cur = self.cur.next
        return self.cur.element

    def remove(self):
        remove_data = self.cur
        self.before.next = self.cur.next
        self.cur = self.before
        self.num_of_data -= 1
        return remove_data.element

    def count(self):
        return self.num_of_data


n, k, m = map(int, input().split())

c_list = CircularLinkedList()
for i in range(1, n + 1):
    c_list.insert(i)

print(c_list.l_first())

while c_list.count() > 1:
    cnt = m