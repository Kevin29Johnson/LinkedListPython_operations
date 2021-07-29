class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_begining(self,data):
        node=Node(data,self.head)#the orginal head will become new nodes next
        self.head=node#new node becomes head

    def print_list(self):
        if self.head is None:
            print("list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data) + "->"
            itr=itr.next
        print(llstr)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)#if there is no node then head becomes only1
            return

        itr=self.head

        while itr.next:#while itr has a next keep going till u find end
            itr=itr.next

        itr.next=Node(data,None)#making the new node at last(tail of list)


    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")

        if index==0:
            self.insert_at_begining(data) # if u want to insert at 1st position
            return

        count=0
        itr=self.head

        while itr:
            if count==index-1:# before inserting at index we need to stop itr at previous of index to modify the nodes
                node=Node(data,itr.next)
                itr.next=node
                
            itr=itr.next
            count+=1

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")

        if index==0:
            self.head=self.head.next #deleting the only the node ie the head

        itr=self.head
        count=0

        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
    

    
    def reverse(self):
        prev=None
        head=self.head

        while head:
            next_node=head.next
            head.next=prev # reversing the links
            prev=head
            head=next_node

        itr=prev # prev is the new head
        llstr=""
        while itr:
            llstr+=str(itr.data) + "->"
            itr=itr.next
        print(llstr)

    def max(self):
        if self.head is None:
            print("list is empty")
        maxl=self.head.data
        itr=self.head
        while itr:
            if maxl<itr.data:
                maxl=itr.data
            itr=itr.next

        print("The maximum value is :",maxl)

    def min(self):
        if self.head is None:
            print("list is empty")

        minl=self.head.data
        itr=self.head
        while itr:
            if minl>itr.data:
                minl=itr.data
            itr=itr.next
        print("The minimum value is :",minl)

    def mean(self):
        if self.head is None:
            print("list is empty")

        sumf=0
        lenl=self.get_length()
        itr=self.head
        while itr:
            sumf+=itr.data
            itr=itr.next

        avg=sumf/lenl

        print("Mean of linked list :",avg)


    def remove_duplicates(self):
        prev=None# keep  track fo the previous node
        dup=dict()#using a dictionary to keep track of all the nodes
        cur=self.head

        while cur:
            if cur.data in dup:#if data already exists that means a duplicate is present
                prev.next=cur.next.next # change of  the links in order to remove the duplicate
                cur=None# deleting that node

            else:
                dup[cur.data]=1 # if we encounter a node for the first time then we put it in the dictionary
                prev=cur         # change the prev
            cur=prev.next       # as good as saying cur=cur.next
        

    
        
        
        


if __name__ == "__main__":

    l1=LinkedList()

    while True:
        print("\nMAIN MENU")

        print("1. Insert at begining of list")

        print("2.Insert at the end of list")

        print("3.Insert at any index ")

        print("4.Insert a list of values")

        print("5.Print linked list")

        print("6.get length of list")

        print("7.Remove a node at a particular index")

        print("8.Reverse linked list")
        
        print("9. Maximum of list")
        
        print("10.Minimum of list")
        
        print("11.Mean of the list")
        
        print("12. remove duplicates")

        print("13.Exit")

        ch= int(input("Enter your Choice:"))

        if ch==1:
            d=int(input("enter data to be inserted"))
            l1.insert_at_begining(d)

        elif ch==2:
            d=int(input("enter data to be inserted"))
            l1.insert_at_end(d)

        elif ch==3:
            d=int(input("enter data to be inserted"))
            i=int(input("enter index to be inserted"))
            l1.insert_at_begining(d,i)

        elif ch==4:
            lst=list(map(int,input("Enter list of values to be inserted").split()))
            l1.insert_values(lst)

        elif ch==5:
            l1.print_list()

        elif ch==6:
            L=l1.get_length()
            print("the length:",L)

        elif ch==7:
            i=int(input("enter index of the element to be removed"))
            l1.remove_at(i)

        elif ch==8:
            l1.reverse()

        elif ch==9:
            l1.max()

        elif ch==10:
            l1.min()

        elif ch==11:
            l1.mean()

        elif ch==12:
            l1.remove_duplicates()
            print("after removal of duplicates :")
            l1.print_list()

        elif ch==13:
            break
            

        else:
            print("Wrong Choice")
    
            

    

    

    
        
        
    
            


    
        
    
