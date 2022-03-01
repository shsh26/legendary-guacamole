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
        self.head = Node('head')
        self.head.next = self.head

    def insert(self, item, new):
        new_node = Node(new)
        cur_node = self.find(item)
        new_node.next = cur_node.next
        cur_node.next = new_node

    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next
        return cur_node

    def find_previous(self, item):
        cur_node = self.head
        while cur_node.next.element != item:
            cur_node = cur_node.next
        return cur_node

    def remove(self, item):
        prev_node = self.find_previous(item)
        prev_node.next = prev_node.next.next

    def show(self):
        cur_node = self.head
        while cur_node.next.element != 'head':
            print(cur_node.element, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.element)


n, k, m = map(int, input().split())
