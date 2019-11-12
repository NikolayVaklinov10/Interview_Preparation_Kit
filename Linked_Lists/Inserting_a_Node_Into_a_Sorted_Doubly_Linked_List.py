import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    # If cur_head reaches end, tail is to point the last node
    cur_head = tail = head
    while cur_head and cur_head.data <= data:
        tail = cur_head
        cur_head = cur_head.next

    node = DoublyLinkedListNode(data)
    ## cur_head reached NULL and so tail is the last node,
    ## and new node must be inserted at the end
    if not cur_head:
        tail.next = node
        node.prev = tail

    ## cur_head is still the first node,
    ## and new node should be the head
    elif not cur_head.prev:
        cur_head.prev = node
        node.next = cur_head
        return node

    ## else new node must be prev to cur_head
    else:
        temp = cur_head.prev
        cur_head.prev = node
        node.prev = temp
        temp.next = node
        node.next = cur_head

    return head