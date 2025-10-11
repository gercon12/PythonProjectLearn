class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Function to find the middle node of a linked list
def middle_linked_list(head: Node) -> int:
    slow = fast = head
    # Move 'fast' two steps and 'slow' one step at a time
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # When 'fast' reaches the end, 'slow' will be at the middle
    return slow.val


# Function to build a linked list from a list of values
def build_list(nodes):
    if not nodes:
        return None
    head = Node(nodes[0])
    current = head
    for val in nodes[1:]:
        current.next = Node(val)
        current = current.next
    return head


if __name__ == "__main__":
    # Example: build a linked list from user input
    values = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
    head = build_list(values)

    if head:
        print("Middle element:", middle_linked_list(head))
    else:
        print("The list is empty.")


