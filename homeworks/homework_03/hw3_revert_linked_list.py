#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    try:
        prev = head.next_node
    except AttributeError:
        return head
    prev = None
    while head:
        curr = head.next_node
        head.next_node = prev
        prev = head
        head = curr
    return prev
