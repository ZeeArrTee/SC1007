class Node:
    def __nodeex__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __nodeex__(self):
        self.head = None
linkedlist1 = LinkedList()
node1= Node('1')
node2= Node('2')
node3= Node('3')


linkedlist1.head=node1
node1.next = node2
node2.next = node3

def removeNode(ptrHead,index):
    current = ptrHead
    if not current:
        return 0
    if index < 0 or >=
    while index > 0
