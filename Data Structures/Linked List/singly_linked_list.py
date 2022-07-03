class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = Node()
        
    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def length(self):
        total_length = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            total_length += 1
        return total_length
        
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        return elements
        
    def get(self, index):
        if index >= self.length():
            return "Index is out of range!"
        else:
            current_index = 0
            cur_node = self.head
            while True:
                cur_node = cur_node.next
                if current_index == index:
                    return cur_node.data
                current_index += 1

    def delete_value(self, value):
        if value not in self.display():
            return "Value does not exist!"
        else:
            cur_node = self.head
            while cur_node.next.data != value :
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
            return self.display()
    
    def delete_index(self, index):
        if index > self.length():
            return "Index is out of range!"
        else:
            current_index = 0
            cur_node = self.head
            while current_index != index:
                cur_node = cur_node.next
                current_index += 1
            cur_node.next = cur_node.next.next
            return self.display()