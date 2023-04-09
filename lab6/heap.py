#skończone

class Element:
    def __init__(self, prior, data):
        self.__dane = data
        self.__priorytet = prior
        
    def __lt__(self, other):
        return self.__priorytet  < other.__priorytet 
        
    def __gt__(self, other):
        return self.__priorytet  > other.__priorytet 
        
    def __str__(self):
        return f'{self.__priorytet} : {self.__dane}'
        
class Heap:
    def __init__(self):
        self.tab = []
        self.size = 0
    
    def is_empty(self):
        return True if not self.size else False
    
    def peek(self):
        return self.tab[0]
    
    def dequeue(self):
        if self.is_empty():
            return None
        max_value =  self.peek()
        
        self.tab[0] = self.tab[self.size-1]
        self.size -= 1
        
        self.rebalance(0)
        return max_value
    
    def enqueue(self, elem):
        if self.size == len(self.tab):
            self.tab.append(elem)
        elif self.size < len(self.tab):
            self.tab[self.size]
        self.size += 1
        
        elem_idx = self.size - 1
        parent_elem_idx = self.parent(elem_idx)
        while elem_idx > 0 and self.tab[elem_idx] > self.tab[parent_elem_idx]:
            self.tab[elem_idx], self.tab[parent_elem_idx] = self.tab[parent_elem_idx], self.tab[elem_idx]
            elem_idx = parent_elem_idx
            parent_elem_idx = self.parent(elem_idx)
            
        
    
    def rebalance(self, idx):
        while True:
            left_child = self.left(idx)
            right_child = self.right(idx)
            max_val_idx = idx
            if left_child <= self.size-1 and self.tab[max_val_idx] < self.tab[left_child]:
                max_val_idx = left_child
            if right_child <= self.size-1 and self.tab[max_val_idx] < self.tab[right_child]:
                max_val_idx = right_child
                
            if max_val_idx != idx:
                self.tab[idx], self.tab[max_val_idx] = self.tab[max_val_idx], self.tab[idx]
                idx = max_val_idx
            else:
                break
        
    
    def left(self, idx):
        return 2 * idx + 1
    
    def right(self, idx):
        return 2 * idx + 2
    
    def parent(self, idx):
        return  (idx - 1) // 2
    
    
    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
            
    def print_tab(self):
        if self.is_empty():
            print("{ }")
            return
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')
        

if __name__ == '__main__':
    max_heap = Heap()
    priors = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    datas = "GRYMOTYLA"
    for prior, data in zip(priors, datas):
        max_heap.enqueue(Element(prior, data))
    max_heap.print_tree(0,0)
    max_heap.print_tab()
    max_val = max_heap.dequeue()
    print(max_heap.peek())
    max_heap.print_tab()
    print(max_val)
    while not max_heap.is_empty():
        print(max_heap.dequeue())
    max_heap.print_tab()
