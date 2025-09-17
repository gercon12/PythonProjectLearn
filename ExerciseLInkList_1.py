class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        return

    # Insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node

        self.head = node

    #print forward
    def print_forward(self):
        if self.head == None:
            print("LinkedList is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "---> "
            itr = itr.next
        print(llstr)

    #print backward
    def print_backward(self):
        if(self.head == None):
            print("LinkedList is empty")
            return

        #reach the last node
        itr = self.head
        while itr.next:
            itr = itr.next

        #go back
        llstr = ""
        while itr:
            llstr += str(itr.data) + "<--- "
            itr = itr.prev
        print(llstr)

    # insert at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None,itr)

#------------------------------------------------------------

    #Get length of linked list
    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        return length

    #Remove data at:
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    #Insert data at:
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next,itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1
#----------------------------------------------------------------

    # insert values
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(5,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()

