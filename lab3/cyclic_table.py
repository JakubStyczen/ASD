#skończone

class CyclicQueue:
    def __init__(self, size = 5, save_id = 0, read_id = 0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.save_id = save_id
        self.read_id = read_id
    
    def realloc(self, save_id):
        new_size = 2*self.size
        new_tab = [None for _ in range(new_size)]
        for idx, elem in enumerate(self.tab[save_id:]):
            new_tab[idx+self.size+1] = elem
        for idx, elem in enumerate(self.tab[:save_id]):
            new_tab[idx] = elem
            
        self.read_id += self.size
        self.size = new_size
        self.tab = new_tab
    
    def is_empty(self) -> bool:
        return self.save_id == self.read_id 
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read_id]
            
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            elem_to_read = self.tab[self.read_id]
            self.tab[self.read_id] = None
            if self.read_id+1 == self.size:
                self.read_id = 0
            else:
                self.read_id += 1
            return elem_to_read
            
    def enqueue(self, data):
        self.tab[self.save_id] = data
        if self.save_id + 1 == self.size:
            self.save_id = 0
        else: 
            self.save_id += 1
        if self.save_id == self.read_id:
            self.realloc(self.save_id)
            
    def __str__(self) -> str:
        str_rep = "[ "
        
        if self.read_id < self.save_id:
            for elem in self.tab[self.read_id: self.save_id]:
                str_rep += f"{elem}, "

        if len(str_rep) > 2:
            str_rep = str_rep[:-2]
        else:
            return "[]"
        str_rep +=" ]"
        return str_rep
    
    def raw_tab_show(self) -> str:
        return str(self.tab)
    
if __name__ == '__main__':
    queue = CyclicQueue()
    for i in range(1,5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for i in range(5,9):
        queue.enqueue(i)
    print(queue.raw_tab_show())
    elem = queue.dequeue()
    while elem:
        print(elem)
        elem = queue.dequeue()
    print(queue)
