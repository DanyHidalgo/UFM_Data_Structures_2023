'''
Binary Search Tree
'''

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return '({})'.format(self.data)
    

class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, value: int):

        """
        Insert a value into the tree
        Args:
            value: Value to be inserted
        """

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):
        """
        Insert a value into the subtree rooted at the given node

        Args:
            value (int): Value to be inserted
            subtree (Node): The root of the subtree to insert into
        """

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        """
        Traverse the tree in pre order

        Args:
            subtree (Node): The root of the subtree to traverse
        """
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


    def search(self, key: int) -> bool:
        """
        Search a key in the tree

        Args:
            key (int): Key to search

        Returns:
            bool: True if the key was found, false if not
        """

        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:
        """
        Search a key in the tree

        Args:
            key (int): Key to search
            subtree (Node): Subtree to search in

        Returns:
            bool: True if the key was found, false if not
        """

        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        

    def find_min(self, subtree: Node) -> int:
        """
        Search for the minimum value in the subtree

        Args:
            subtree (Node): Root of the subtree to search in

        Returns:
            int: The node containing the minimum value in the subtree
        """

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree


    def find_max(self, subtree: Node) -> int:
        """
        Search for the maximum value in the subtree

        Args:
            subtree (Node): Root of the subtree to search in

        Returns:
            int: The node containing the minimum value in the subtree
        """

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    
    def delete(self, key: int):
        """
        Deletes a node from the tree

        Args:
            key (int): Key to be deleted
        """

        if self.root is None:
            print("The tree is empty")
        
        else:
            self._delete(key, self.root)
    
    def _delete(self, key: int, subtree: Node):
        """
        Deletes a node from the tree

        Args:
            key (int): Key to be deleted
            subtree (Node): Root of the subtree to search in
        """
        
        if key < subtree.data:
            if subtree.left_child is not None:
                self._delete(key, subtree.left_child)
            else:
                print("Key is not in the tree")
        
        elif key > subtree.data:
            if subtree.right_child is not None:
                
                self._delete(key, subtree.right_child)

        else:
            if subtree.left_child is None and subtree.right_child is None:
                subtree = None

            elif subtree.left_child is not None and subtree.right_child is None:
                subtree = subtree.left_child

            elif subtree.left_child is None and subtree.right_child is not None:
                subtree = subtree.right_child

            else:
                min_node = self.find_min(subtree.right_child)
                subtree.data = min_node.data
                self._delete(min_node.data, subtree.right_child)       