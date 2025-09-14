class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
        
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True
    
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def removeNode(self,index):
        if int(index) < 0 or int(index) >= int(self.size):
            raise ValueError("Invalid position")
        
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        
        preious = self.findNode(index-1)
        if index == self.size - 1:
            preious.next = None
        elif preious and preious.next.next:
            preious.next = preious.next.next
            self.size -= 1
            return True
        return False

def moveMinNode(head):
        current = head
        smallhead = current
        count = 0
        min_i = 0
        while current: #search for smallest
            if current.data <= smallhead.data:
                smallhead = current
            current = current.next

        #data found but list unchanged
        current = head
        while current:
            print("c = ",count)
            if current.data == smallhead.data:
                linked_list.removeNode(count)
                linked_list.insertNode(smallhead.data,0)
            current = current.next
            count += 1
        return linked_list.head

if __name__ == "__main__":
    linked_list = LinkedList()
    
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
    
    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break
    
    print("\nBefore:", end=" ")
    linked_list.printList()
    
    linked_list.head = moveMinNode(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()