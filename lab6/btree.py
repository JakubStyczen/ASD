#skończone

SIZE = 3

class Node:
    def __init__(self) -> None:
        self.keys = []
        self.children = [None for _ in range(SIZE+1)]
              
class BTree:
    def __init__(self, root=None, max_size=SIZE) -> None:
        self.root = None
        self.max_size = SIZE
        
    def insert(self, number):
        #empty root, add new one
        if self.root is None:
            new_node = Node()
            new_node.keys.append(number)
            self.root = new_node
        #full root, split and insert
        elif len(self.root.keys) == SIZE:
            new_root = Node()
            old_root = self.root
            self.root = new_root
            self.root.children[0] = old_root
            elem, node = self.divide_node(self.root.children[0])
            self.root.keys.append(elem)
            self.root.children[1] = node
            self.__insert(self.root, number)
        else:
            self.__insert(self.root, number)
            
            
    def __insert(self, current_node, number):        
        #for leaf
        if all([False for num in current_node.children if num is not None]):
            place = len(current_node.keys)
            for idx, elem in enumerate(current_node.keys):
                if elem >= number:
                    place = idx
                    break
            #not full leaf
            if len(current_node.keys) < self.max_size:
                current_node.keys.insert(place, number)
                return (None, None, None)
            
            #full leaf
            elif len(current_node.keys) == self.max_size:
                middle, node = self.divide_node(current_node)
                if place <= self.max_size//2:
                    current_node.keys.append(number)
                    current_node.keys.sort()
                else:
                    node.keys.append(number)
                    node.keys.sort()  
                return middle, node, None
    
        #not leaf
        else:
            #search for idx
            place = len(current_node.keys)
            for idx, elem in enumerate(current_node.keys):
                if elem >= number:
                    place = idx
                    break
            middle, node, addtional = self.__insert(current_node.children[place], number)

            #if child was splitted
            if middle is not None:
                
                #not full node, find new place for middle elem and rerange children
                if len(current_node.keys) < self.max_size:
                    place = len(current_node.keys)
                    for idx, elem in enumerate(current_node.keys):
                        if elem >= middle:
                            place = idx
                            break
                    current_node.keys.insert(place, middle)
                    current_node.children[place+1:] =  current_node.children[place:]
                    current_node.children[place+1] = node
                    
                    #if there was splitted not leaf
                    if addtional is not None:
                        middle_before, node_before = addtional
                        place = len(current_node.keys)
                        for idx, elem in enumerate(current_node.keys):
                            if elem >= middle_before:
                                place = idx
                                break

                        place_for_before = len(current_node.children[place].keys)
                        for idx, elem in enumerate(current_node.children[place].keys):
                            if elem >= middle_before:
                                place_for_before = idx
                                break
                        current_node.children[place].keys.insert(place_for_before, middle_before)
                        current_node.children[place].children[place_for_before+1:] =  current_node.children[place].children[place_for_before:]
                        
                        current_node.children[place].children[place_for_before+1] = node_before
                    return None, None, None
            
                #for full not leaf, split and return additional child
                elif len(current_node.keys) == self.max_size:
                    new_middle, next_node = self.divide_node(current_node)
                    return new_middle, next_node, (middle, node)
            else:
                return None, None, None
                      
    def divide_node(self, node):
        middle_idx = self.max_size//2
        middle_elem = node.keys[middle_idx]
        
        new_node = Node()
        new_node.keys= node.keys[middle_idx+1:]
        node.keys = node.keys[:middle_idx]
        
        #if not leaf, repair children
        if not all([False for num in node.children if num is not None]):
            new_node.children[0:self.max_size//2+1] = node.children[self.max_size//2+1:self.max_size+1]
            node.children[self.max_size//2+1:] = [None for _ in range(self.max_size//2+1)]

        return middle_elem, new_node
                 
        
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(len(node.keys)+1):                 	
                self._print_tree(node.children[i], lvl+1)
                if i<len(node.keys):
                    print(lvl*'   ', node.keys[i])

if __name__ == '__main__':
    b_tree = BTree()
    nodes = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for node in nodes:
        b_tree.insert(node)
    b_tree.print_tree()
    
    b_tree2 = BTree()
    for i in range(20):
        b_tree2.insert(i)
    b_tree2.print_tree()
    for i in range(20, 200):
        b_tree2.insert(i)
    b_tree2.print_tree()
    
    SIZE=5
    b_tree3 = BTree()
    for i in range(0, 200):
        b_tree3.insert(i)
    b_tree3.print_tree()
