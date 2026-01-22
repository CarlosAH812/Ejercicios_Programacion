
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            print(f"Inserted {data} as root")
            return
        
        queue_front = QueueNode(self.root)
        queue_rear = queue_front
    
        while queue_front is not None:
            current = queue_front.node
            
            if current.left is None:
                current.left = new_node
                print(f"Inserted {data} as left child of {current.data}")
                return
            else:
                new_queue_node = QueueNode(current.left)
                queue_rear.next = new_queue_node
                queue_rear = new_queue_node
            
            if current.right is None:
                current.right = new_node
                print(f"Inserted {data} as right child of {current.data}")
                return
            else:
                new_queue_node = QueueNode(current.right)
                queue_rear.next = new_queue_node
                queue_rear = new_queue_node
            
            queue_front = queue_front.next
    
    def print_tree(self):
        if self.root is None:
            print("Tree is empty!")
            return
        
        print("\n" + "="*50)
        print("BINARY TREE VISUALIZATION")
        print("="*50)
        
        print("\n1. In-Order Traversal (Left - Root - Right):")
        print("   ", end="")
        self._inorder(self.root)
        print()
    
        print("\n2. Pre-Order Traversal (Root - Left - Right):")
        print("   ", end="")
        self._preorder(self.root)
        print()
        
        print("\n3. Post-Order Traversal (Left - Right - Root):")
        print("   ", end="")
        self._postorder(self.root)
        print()
        
        print("\n4. Level-Order Traversal (By Levels):")
        self._levelorder()
        
        print("\n5. Tree Structure:")
        self._print_structure(self.root, "", True)
        
        print("="*50 + "\n")
    
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)     
            print(node.data, end=" ")     
            self._inorder(node.right)     
    
    def _preorder(self, node):
        if node is not None:
            print(node.data, end=" ")    
            self._preorder(node.left)     
            self._preorder(node.right)     
    
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)   
            self._postorder(node.right)    
            print(node.data, end=" ")     
    
    def _levelorder(self):
        if self.root is None:
            return
        
        queue_front = QueueNode(self.root)
        queue_rear = queue_front
        
        level = 1
        print(f"   Level {level}: ", end="")
        
        while queue_front is not None:
            current = queue_front.node
            print(current.data, end=" ")
            
            if current.left is not None:
                new_queue_node = QueueNode(current.left)
                queue_rear.next = new_queue_node
                queue_rear = new_queue_node
            
            if current.right is not None:
                new_queue_node = QueueNode(current.right)
                queue_rear.next = new_queue_node
                queue_rear = new_queue_node
            
            queue_front = queue_front.next
    
    def _print_structure(self, node, prefix, is_tail):
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.data))
            
            extension = "    " if is_tail else "│   "
            
            if node.left is not None and node.right is not None:
                self._print_structure(node.left, prefix + extension, False)
                self._print_structure(node.right, prefix + extension, True)
            elif node.left is not None:
                self._print_structure(node.left, prefix + extension, True)
            elif node.right is not None:
                self._print_structure(node.right, prefix + extension, True)

class QueueNode:
    def __init__(self, tree_node):
        self.node = tree_node
        self.next = None

if __name__ == "__main__":
    tree = BinaryTree()
    
    print("Building Binary Tree...\n")
    
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    
    tree.print_tree()
    
    print("\nAdding more nodes...\n")
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)
    
    tree.print_tree()