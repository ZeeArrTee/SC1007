class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def printList2(ll):
    if ll.head is not None:
        cur = ll.head
        print(f"Current List has {ll.size} elements: ", end="")
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

def findNode2(ll, index):
    if ll.head is not None:
        cur = ll.head
        if cur is None or index < 0 or index >= ll.size:
            return None
        while index > 0:
            cur = cur.next
            if cur is None:
                return None
            index -= 1
        return cur
    else:
        return None



def insertNode2(ll, index, item):
    newNode = ListNode(item)
    # If empty listdef or inserting first node, update head pointer
    if index == 0:
        newNode.next = ll.head
        ll.head = newNode
        ll.size += 1
        return True
    # Find the nodes before and at the target position
    # Create a new node and reconnect the links
    pre = findNode2(ll, index - 1)
    if pre is not None:
        newNode.next = pre.next
        pre.next = newNode
        ll.size += 1
        return True
    return False

def removeNode2(ll, index):
    current = ll.head
    prev = None
    count = 0
    if index == 0:
        if current.next == None:
            return 0
        else:
            ll.head = current.next

    while count < index:
        prev = current
        if current.next == None:
            return 0
        current =current.next

        count += 1

    prev.next = current.next
    if prev == None:
        return 0
    if current.next == None:
        return 0

#startworkhere

def moveMaxtoFront(ll):
    