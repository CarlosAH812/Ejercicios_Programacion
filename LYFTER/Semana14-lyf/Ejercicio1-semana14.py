
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        
        new_node.next = self.top
    
        self.top = new_node
        
        self.size += 1
        
        print(f"Pushed: {data}")

    def pop(self):
        if self.top is None:
            print("Stack is empty! Cannot pop.")
            return None
        
        popped_data = self.top.data
        
        self.top = self.top.next
        
        self.size -= 1
        
        print(f"Popped: {popped_data}")
        return popped_data
    
    def print_stack(self):
        if self.top is None:
            print("Stack is empty!")
            return
        
        print("\n--- Stack Contents (Top to Bottom) ---")
        
        current = self.top
        position = 1
        
        while current is not None:
            print(f"{position}. {current.data}")
            current = current.next
            position += 1
        
        print(f"Total elements: {self.size}\n")

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    stack.print_stack()
    
    stack.pop()
    stack.pop()
    
    stack.print_stack()
    
    stack.push(50)
   
    stack.print_stack()