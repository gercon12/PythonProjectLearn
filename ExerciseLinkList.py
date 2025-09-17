#Define node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Define the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    #Insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    #Show the list
    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "---> "
            itr = itr.next
        print(llstr)

    #insert at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    #insert values
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

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
            return

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
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
        while itr.next:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_values(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next

    def remove_by_values(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        #count = 0
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
         
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango","grapes","orange"])
    ll.print()
    print("length of linked list:", ll.get_length())
    #ll.remove_at(20)
    ll.insert_after_values("mango","apple")
    ll.print()
    ll.remove_by_values("orange")
    ll.print()
    ll.remove_by_values("figs")
    ll.print()
    ll.remove_by_values("banana")
    ll.print()
    ll.remove_by_values("mango")
    ll.print()
    ll.remove_by_values("apple")
    ll.print()
    ll.remove_by_values("grapes")
    ll.print()
