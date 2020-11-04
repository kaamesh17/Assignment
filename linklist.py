class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
class LinkedList:
        def __init__(self):
            self.head = None
            self.last_node = None
        def append(self,data):
            if self.last_node is None:
                self.head = Node(data)
                self.last_node = self.head
            else:
                self.last_node.next = Node(data)
                self.last_node = self.last_node.next
        def display(self):
            Current = self.head
            while Current is not None:
                print(Current.data,end = " ")
                Current = Current.next
a_list = LinkedList()
a = int(input("Number of elements you like to enter  :  "))
for i in range(a):
    data = int(input("Enter data items  :  "))
    a_list.append(data)
print("Linked Lists are  :  ",end = "   ")
a_list.display()


# searching  the index value of output
# deletion of element from output
# doubly linedlist
