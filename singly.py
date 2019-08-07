class Slist:
    def __init__(self):
        self.head = None

    def add_to_front(self,value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        if self.head == None:
            print("Invalid, we need values!")
            return self
        x = self.head
        while(x != None):
            print(x.value)
            x = x.next
        return self

    def add_to_back(self, value):
        if self.head == None:
            self.add_to_front(value)
            return self

        new_node = SLNode(value)
        x = self.head
        while(x.next != None):
            x = x.next
        x.next = new_node
        return self

    def find_value(self, value):
        if self.head == None:
            print("Invalid, we need values!")
            return self
        x = self.head
        while (x != None):
            x = x.next
            if x.value == value:
                return True
        if x == None:
            return False

    def insert_at(self, value, int):
        x = self.head
        count = 0
        while (x != None):
            x = x.next
            count += 1
            if count == int-1:
                new_node = SLNode(value)
                new_node.next = x.next
                x.next = new_node
                return self

    def remove_from_front(self):
        if self.head == None:
            print("Invalid, we need values!")
            return self
        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            print("Invalid, we need values!")
            return self
        x = self.head
        while (x != None):
            if x.next.next == None:
                x.next = None
                return self
            x = x.next
        return self

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

testlist = Slist()
testlist.add_to_front("sam").add_to_front("tim").add_to_front("leah").add_to_front("peter").add_to_back("woah")
# print(testlist.find_value("sam"))
testlist.insert_at("insert_at",2).print_values()
