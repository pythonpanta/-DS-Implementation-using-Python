'''
singly list list 
opetation :
1.Insertion
  1.1:At the biginning
  1.1:At the end
  1.1:At the any position
2.Deletion
  2.1:From the biginning
  2.1:From the end
  2.1:From the any position
3.Traversal
'''
# class for making the individual node 
class Node:
    # class for making the node with data with None reference 
    def __init__(self,data):
        self.data=data
        self.ref=None


# to make the connection or the list berween the differert node     
class LinkList:
    # to linked different nodes 
    def __init__(self):
        self.head=None

# To print All the data from the listlist 
    def Print_LL(self):
        '''function for traversaling the Linked List'''
        if self.head is None:
            print('Linked list is Empty at the moment')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.ref


# For adding the new Node in Linkliost
    def add_begin(self,data):
        '''
        function to add node at the beginning of the node 
        step:
        1.create the new node as new_node
        2.new_node->head
        3.head->new_node
        '''
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        '''
        function to add new node at the end of the linked list
        step:
        1.create the new node as new_node
        2.traverse to the end of the last node
           n=self.head
           while n.ref is not None:

        '''
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.ref=None
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n is None:
            print('Node is not present in the list')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print('Linklist is empty at the moment')
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            else:
                n=n.ref
        if n is None:
            print('Node is not present in the list')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node



ll1=LinkList()
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
ll1.add_end(100)
ll1.add_after(200,30)
ll1.add_before(80,30)
ll1.Print_LL()

        