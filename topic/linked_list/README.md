Linked List
======

## Common Rule

- If the list is cyclic, the 2-pace pointer will eventually meet the 1-pace. see [lintcode/102_linked_list_cycle.py](../lintcode/102_linked_list_cycle.py)
- If there is a intersection node, the steps from the first node is equal to from meet node plus 1. see [lintcode/103_linked_list_cycle_ii.py](../lintcode/103_linked_list_cycle_ii.py)
- If its a list, the middle node is the 1-pace pointer when the 2-pace pointer has traversed the list. see [lintcode/98_sort_list.py](../lintcode/98_sort_list.py)

## Reverse Linked List

- with two extra vars

```python
>>> cur = nxt = None
>>> while head:
...     nxt = head.next
...     head.next = cur
...     cur = head
...     head = nxt
```

- with one extra var (**Python only**)

```python
>>> cur = None
>>> while head:
...     cur, cur.next, head = head, cur, head.next
```
