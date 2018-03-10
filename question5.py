question5.py

#Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

#class Node(object):
  #def __init__(self, data):
    #self.data = data
    #self.next = None




class Element(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# create linked list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.linkListCount = 0
        
    # add node
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            self.linkListCount += 1
            
        else:
            self.head = new_element

    # input for index
    def question5(self, m):
        #check if index is none
        counter = 1
        current = self.head
        if m < 1:
            return None
        while current and counter <= m:
            if counter == m:
                return current.data
            current = current.next
            counter += 1
        return "index does not exist";

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# call function output: 3
print(ll.question5(3))
# call function output: index does not exit
print(ll.question5(17))

# call function output: None
print(ll.question5(None))
