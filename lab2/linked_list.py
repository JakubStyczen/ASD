#skończone
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next= next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def destroy(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_pos = self.head
            while current_pos.next is not None:
                current_pos = current_pos.next
                
            current_pos.next = Node(data)
        
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            
    def remove_end(self):
        if self.head is not None:
            current_pos = self.head
            prev = self.head
            while current_pos.next is not None:
                prev = current_pos
                current_pos = current_pos.next

            prev.next = None
            
    def is_empty(self) -> bool:
        return True if self.head is None else False
        
    def length(self) -> int:
        cnt = 0
        if self.head is None:
            return cnt
        else:
            current_pos = self.head
            cnt += 1
            while current_pos.next is not None:
                cnt += 1
                current_pos = current_pos.next
            return cnt
    
    def get(self):
        return self.head.data if self.head is not None else None
        
    def show_list(self):
        if self.head is not None:
            current_pos = self.head
            while current_pos is not None:
                print(f'->{current_pos.data}')
                current_pos = current_pos.next


if __name__ == "__main__":
    unis = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    
    uczelnie = LinkedList()
    
    for uni in unis[:3]:
        uczelnie.append(uni)
                
    for uni in unis[3:]:
        uczelnie.add(uni)
             
    uczelnie.show_list() 
    
    print(uczelnie.length())
    
    uczelnie.remove()
            
    print(uczelnie.get())
    
    uczelnie.remove_end()
    
    uczelnie.show_list()
    
    uczelnie.destroy()
    
    print(uczelnie.is_empty())
    
    uczelnie.remove()
    
    uczelnie.remove_end()
    
        
