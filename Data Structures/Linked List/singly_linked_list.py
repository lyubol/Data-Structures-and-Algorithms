class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
            
    def isEmpty(self):
        return self.head is None
        
    def length(self):
        if self.isEmpty() == True:
            return 0
        else:
            total_length = 1
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
                total_length += 1
            return total_length
        
    def display(self):
        curr_node = self.head
        elements = []
        if curr_node is None:
            return elements
        while curr_node:
            elements.append(curr_node.data)
            curr_node = curr_node.next
        return elements
        
#     def get(self, index):
#         if self.isEmpty:
#             return "List is empty!"
#         elif index >= self.length():
#             return "Index is out of range!"
#         else:
#             current_index = 0
#             cur_node = self.head
#             while True:
#                 cur_node = cur_node.next
#                 if current_index == index:
#                     return cur_node.data
#                 current_index += 1

#     def deleteValue(self, value):
#         if value not in self.display():
#             return "Value does not exist!"
#         else:
#             cur_node = self.head
#             while cur_node.next.data != value :
#                 cur_node = cur_node.next
#             cur_node.next = cur_node.next.next
#             return self.display()
    
#     def deleteIndex(self, index):
#         if index > self.length():
#             return "Index is out of range!"
#         else:
#             current_index = 0
#             cur_node = self.head
#             while current_index != index:
#                 cur_node = cur_node.next
#                 current_index += 1
#             cur_node.next = cur_node.next.next
#             return self.display()
        
    def insertAtBegining(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node