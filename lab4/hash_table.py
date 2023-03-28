#skończone

class ElementNotFoundException(Exception):
    pass

class MaxSizeReachedException(Exception):
    pass


class HashTable:
    
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = len(self.tab)
        self.c1 = c1
        self.c2 = c2
        
    def search_for_idx(self, key, idx):
        for i in range(1, self.size+1):
            new_idx = (idx + self.c1 * i + self.c2 * i**(2)) % self.size
            if self.tab[new_idx] is not None and self.tab[new_idx].key == key:
                return self.tab[new_idx].data
            
        return None    
        
    def search(self, key):
        idx = self.hash_function(key)
        if self.tab[idx] is not None:
            if self.tab[idx].key == key:
                return self.tab[idx].data
            else:
                return self.search_for_idx(key, idx)
        else:
            return self.search_for_idx(key, idx)
            
    
    def insert(self, elem):
        idx = self.hash_function(elem.key)
        if self.tab[idx] is None or self.tab[idx].key == elem.key:
            self.tab[idx] = elem
        else:
            for i in range(1, self.size+1):
                new_idx = (idx + self.c1 * i + self.c2 * i**(2)) % self.size
                if self.tab[new_idx] is None:
                    self.tab[new_idx] = elem
                    return
            raise MaxSizeReachedException
            
    def remove(self, key):
        idx = self.hash_function(key)
        if self.tab[idx] is not None:
            if self.tab[idx].key == key:
                self.tab[idx] = None
            else:
                for i in range(1, self.size+1):
                    new_idx = (idx + self.c1 * i + self.c2 * i**(2)) % self.size
                    if self.tab[new_idx] is not None and self.tab[new_idx].key == key:
                        self.tab[new_idx] = None
                        return
                raise ElementNotFoundException
                   
        else:
            raise ElementNotFoundException

    
    def __str__(self):
        str_rep = "{"
        for value in self.tab:
            str_rep += f'{str(value)}, '
        str_rep = str_rep[:-2] + "}"
        return str_rep
    
    def hash_function(self, key):
        if type(key) is str:
            return sum([ord(letter) for letter in key]) % self.size
        else:
            return key % self.size
            
    def colision_solving(self, new_element):
        old_idx = self.hash_function(new_element.key)
        
        for idx in range(1, self.size):
            new_idx = (old_idx + self.c1 * idx + self.c2 * idx**(2)) % self.size
            
            if self.tab[new_idx] is None or self.tab[new_idx].key == new_element.key:
                self.tab[new_idx] = new_element
                return 
        raise MaxSizeReachedException    
        
    
    
class HashTableElement:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def __str__(self):
        return f'{self.key}: {self.data}'
    
if __name__ == "__main__":
    def test_linear(size, c1=1, c2=0):
        h1 = HashTable(size, c1, c2)
        datas = "ABCDEFGHIJKLMNO"
        
        for idx, elem in enumerate(datas, 1):
            try:
                if idx==6:
                    h1.insert(HashTableElement(18, "F"))
                elif idx==7:
                    h1.insert(HashTableElement(31, "G"))
                else:
                    h1.insert(HashTableElement(idx, elem))
            except MaxSizeReachedException:
                print('Brak miejsca')
        try:
            print(h1)
            print(h1.search(5))
            print(h1.search(14))
            h1.insert(HashTableElement(5, 'Z'))
            print(h1.search(5))
            h1.remove(5)
            print(h1)
            print(h1.search(31))
            h1.insert(HashTableElement('test', 'W'))
            print(h1)
        except ElementNotFoundException:
            print('Brak danej')
        
    def test_quad(size, c1=0, c2=1):
        h1 = HashTable(size, c1, c2)
        datas = "ABCDEFGHIJKLMNO"
        
        for idx, elem in enumerate(datas, 1):
            try:
                h1.insert(HashTableElement(idx*13, elem))
            except MaxSizeReachedException:
                print('Tablica mieszająca jest pełna!')
        print(h1)
        
    test_linear(13,1,0)
    test_quad(13,1,0)
    test_quad(13,0,1)
    test_linear(13,0,1)
                
  
