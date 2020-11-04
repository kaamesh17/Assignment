class Node: 
    def __init__(s, data): 
        s.data = data 
        s.next = None
        s.prev = None
class DoublyLinkedList: 
    def __init__(s): 
        s.head = None
    def push(s, new_data): 
        new_node = Node(new_data) 
        new_node.next = s.head 
        if s.head is not None: 
            s.head.prev = new_node 
        s.head = new_node 
    def insertAfter(s, prev_node, new_data): 
        if prev_node is None: 
            print ("the given previous node cannot be NULL")
            return 
        new_node = Node(new_data) 
        new_node.next = prev_node.next
        prev_node.next = new_node 
        new_node.prev = prev_node 
        if new_node.next is not None: 
            new_node.next.prev = new_node 
    def append(s, new_data): 
        new_node = Node(new_data) 
        new_node.next = None
        if s.head is None: 
            new_node.prev = None
            s.head = new_node 
            return 
        last = s.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(s, node): 
        print ("\nTraversal in forward direction")
        while(node is not None): 
            print (" % d" %(node.data)), 
            last = node 
            node = node.next
        print ("\nTraversal in reverse direction")
        while(last is not None): 
            print (" % d" %(last.data)), 
            last = last.prev 
llist = DoublyLinkedList() 
llist.append(6) 
llist.push(7) 
llist.push(1) 
llist.append(4) 
llist.insertAfter(llist.head.next, 8) 
print ("Created DLL is: ")
llist.printList(llist.head) 
