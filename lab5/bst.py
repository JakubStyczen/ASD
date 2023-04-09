#skończone

class Node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'{key} {data}'

class BST:
    def __init__(self, root=None):
        self.root = root
    
    i=0
    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.__search(key, self.root)

            
    def __search(self, key, node):
        #lewe
        if node.key > key:
            node_r = self.__search(key, node.left)
        #prawe
        elif node.key < key:
            node_r = self.__search(key, node.right)
        #równe
        else:
            return node.data
        return node_r
            
    
    def insert(self, key, data):
        # if self.root is None:
        #     self.root = Node(key, data, None, None)
        # elif current_node == 'root':
        #     self.insert(key, data, current_node=self.root)
        # elif current_node.key == key:
        #     current_node.data = data
        # elif current_node.key > key:
        #     if current_node.left is None:
        #         current_node.left = Node(key, data, None, None)
        #     else:
        #         self.insert(key, data, current_node.left)
        # else:
        #     if current_node.right is None:
        #         current_node.right = Node(key, data, None, None)
        #     else:
        #         self.insert(key, data, current_node.right)
        if self.root is None:
            self.root = Node(key, data, None, None)
        else:
            return self.__insert(key, data, self.root)
        
    def __insert(self, key, data, current_node):
        if current_node.key == key:
            current_node.data = data
            return 
        elif current_node.key > key and current_node.left is None:
            current_node.left = Node(key, data, None, None)
            return 
        elif current_node.key > key:
            return self.__insert(key, data, current_node.left)
        elif current_node.key < key and current_node.right is None:
            current_node.right = Node(key, data, None, None)
            return 
        elif current_node.key < key:
            return self.__insert(key, data, current_node.right)
        
    
    def delete(self, key):
        if self.root is None:
            return
        else:
            return self.__delete(key, self.root)
        
    def __delete(self, key, current_node):    
        #lewe
        if current_node.key > key:
            current_node.left = self.__delete(key, current_node.left)
        #prawe
        elif current_node.key < key:
            current_node.right = self.__delete(key, current_node.right)
        #równe
        else:
            #bez dzieci
            if current_node.left is None and current_node.right is None:
                return None
            #tylko prawe 
            elif current_node.left is None:
                return current_node.right
            #tylko lewe
            elif current_node.right is None:
                return current_node.left
            #oba 
            lowest = current_node.right
            while lowest.left is not None:
                lowest = lowest.left
            
            current_node.key = lowest.key
            current_node.data = lowest.data
            
            current_node.right = self.__delete(lowest.key, current_node.right)
            
        return current_node
        
    
    def print(self):
        if self.root is None:
            return ""
        else:
            return self.__print(self.root)
    
    def __print(self, node):
        if node.left is not None:
            self.__print(node.left)
        print(f'{node.key} {node.data},', end="")
        if node.right is not None:
            self.__print(node.right)
    
    def height(self, starting_node_key=None):
        if starting_node_key is None:
            starting_node_key = self.root
        if starting_node_key != self.root:
            return self.__height(self.__height_from_node(starting_node_key, self.root))
        else:
            return self.__height(starting_node_key)
    
    def __height(self, node):
        if node is None:
            return -1 #0
        else:
            L_H = self.__height(node.left)
            R_H = self.__height(node.right)
            return R_H + 1 if R_H > L_H else L_H +1
    
    def __height_from_node(self, key, node):
        if node.key > key:
            return self.__height_from_node(key, node.left)
        elif node.key < key:
            return self.__height_from_node(key, node.right)
        else:
            return node
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)
    
if __name__ == "__main__":
    bst = BST()
    nodes = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, data in nodes.items():
        bst.insert(key, data)
    bst.print_tree()
    bst.print()
    print()
    print(bst.search(24))
    bst.insert(20, "AA")
    bst.insert(6, "M")
    bst.delete(62)
    bst.insert(59, "N")
    bst.insert(100, "P")
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, "R")
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    bst.print()
    print()
    bst.print_tree()
    
