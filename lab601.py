#Shifa Mehreen
#121910313005

#To create a linked list with sample inputs

#Node class
class Node:
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

#Code execution starts here

#starts with empty list
LL=LinkedList()
LL.head=Node(10)
second=Node(20)
third=Node(30)

LL.head.next=second;
second.next=third;

LL.display()