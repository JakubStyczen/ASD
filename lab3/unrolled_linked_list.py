#skończone

ELEMENT_SIZE = 6

class ListElement:
    def __init__(self, tab = None):
        if tab is None:
            self.tab = [None for _ in range(ELEMENT_SIZE)]
        else:
            self.tab = tab
        self.size = ELEMENT_SIZE 
        self.usage = 0
        self.next = None
    
    def insert(self, val, idx):
        if self.usage < ELEMENT_SIZE:
            if self.tab[idx] is not None:
                for id, elem in enumerate(self.tab[:-1]):
                    if id >= idx:
                        self.tab[id+1] = elem
            self.tab[idx] = val
            self.usage += 1
        
    def pop(self, idx):
        res = self.tab[idx]
        if 0 <= idx <= self.size-1: 
            if self.tab[idx] is not None:
                
                for id, elem in enumerate(self.tab):
                    if id > idx:
                        self.tab[id-1] = elem
                self.usage -= 1
                self.tab[self.usage] = None
        return res
            
    def update_usage(self):
        self.usage = len([1 for elem in self.tab if elem != None])
              
    def get(self, idx):
        return self.tab[idx]
                
    def __str__(self):
        return str(self.tab)
                
class UnrolledLinkedList:
    def __init__(self, node = None):
        self.link = node
        self.size = 0
        
    def get(self, idx):
        cnt = 0
        current_tab = self.link
        while current_tab is not None:
            for elem in current_tab.tab:
                if elem is not None and cnt == idx:
                    return elem
                elif elem is not None:
                    cnt += 1
            current_tab = self.link.next
            
            
            


    def insert(self,val, idx):
        current_tab = self.link
        curr_idx = 0

 
        while True:
            usage = current_tab.usage
            if usage == 0:
                current_tab.insert(val, idx)    
                break
 
            if curr_idx <= idx <= curr_idx + usage:

                if usage == ELEMENT_SIZE:
                    new_element = ListElement()
                    new_element.next = current_tab.next
                    current_tab.next = new_element
                    
                    piece = current_tab.tab[ELEMENT_SIZE//2:]
                    new_element.tab[:ELEMENT_SIZE//2] = piece
                    current_tab.tab[ELEMENT_SIZE//2:] = [None for _ in piece]
                    current_tab.update_usage()
                    new_element.update_usage()
                    
                usage = current_tab.usage
                if curr_idx <= idx <= curr_idx + usage:  
                    current_tab.insert(val,idx-curr_idx)
                else:
                    new_element.insert(val, -curr_idx - usage + idx)
                break
                
            if current_tab.next is None:
                print(val)
                if usage < ELEMENT_SIZE:
                    current_tab.insert(val, usage)
                else:
                    new_element = ListElement()
                    new_element.next = current_tab.next
                    current_tab.next = new_element
                    new_element.insert(val, 0)
                    break
                
            
            curr_idx += usage
            current_tab = current_tab.next
            
        self.size += 1
    
    def delete(self, idx):
        current_tab = self.link
        curr_idx = 0
 
        while current_tab is not None:
            if curr_idx <= idx < curr_idx + ELEMENT_SIZE:
                current_tab.pop(idx%ELEMENT_SIZE)
                
                next_tab = current_tab.next
                if current_tab.usage < ELEMENT_SIZE//2 and next_tab is not None:
                    if next_tab.usage - 1 < ELEMENT_SIZE//2:
                        piece = next_tab.tab[:ELEMENT_SIZE//2]
                        current_tab.tab[current_tab.usage:current_tab.usage+len(piece)] = piece
                        
                        current_tab.update_usage()
                        if next_tab.next is not None:
                            current_tab.next = next_tab.next
                        else:
                            current_tab.next = None
                        
                            
                        
                    else:
                        current_tab.insert(current_tab.next.pop(0), current_tab.usage)

                    break
                
            curr_idx += ELEMENT_SIZE
            current_tab = current_tab.next
            
        self.size -= 1
    
    def printList(self):
        current = self.link
        
        while current is not None:
            print(f'->{current}')
            current = current.next
        print()
            
if __name__ == '__main__':
    ull = UnrolledLinkedList(ListElement())
    for i in range(1,10):
        ull.insert(i, i-1)
    print(ull.get(4))
    ull.insert(10, 1)
    ull.insert(11, 8)
    ull.printList()
    ull.delete(1)
    ull.delete(2)
    ull.printList()
    
