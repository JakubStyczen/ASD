#skończone
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class TwoWayLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def destroy(self):
        current_pos = self.head
        while current_pos.next is not None:
            current_pos = current_pos.next
            current_pos.prev.next = None
            
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            old_head.prev = new_node
            self.head = new_node
            new_node.next = old_head
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None
            
            
    def remove_end(self):
        if self.head is not None:
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None
            
            
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
    
    uczelnie = TwoWayLinkedList()
    
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

        
