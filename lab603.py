#Shifa Mehreen
#121910313005

#inserting a node at the beigning

#Node class
class node:
    #Function to initialise the node object
    def __init__(self,data):
        self.data=data
        self.next=None

#Linked List class contains a Node object
class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head=None

    #function to display elements
    def display(self):
        ele = []
        cur_node = self.head
        while cur_node != None:
            ele.append(cur_node.data)
            cur_node = cur_node.next
        print ("Linked List:" ,ele)

#to insert new element at start of the list
    def AtBegining(self,new_element):
        print("Added element: ",new_element)
        new_node = node(new_element)
# Update the new nodes next val to existing node
        new_node.next = self.head
        self.head = new_node

#Code execution starts here

#starts with empty list
LL=LinkedList()
LL.head=node(10)
second=node(20)
third=node(30)

LL.head.next=second;
second.next=third;

LL.display()

LL.AtBegining(50)
LL.display()

