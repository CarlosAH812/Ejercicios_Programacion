
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_left(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
           
            new_node.next = self.head  
            self.head.prev = new_node  
            self.head = new_node
        
        self.size += 1
        print(f"Pushed left: {data}")
    
    def push_right(self, data):
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node
        
        self.size += 1
        print(f"Pushed right: {data}")
    
    def pop_left(self):
        if self.head is None:
            print("Deque is empty! Cannot pop left.")
            return None
        
        popped_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        print(f"Popped left: {popped_data}")
        return popped_data
    
    def pop_right(self):
        if self.tail is None:
            print("Deque is empty! Cannot pop right.")
            return None
        
        popped_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        print(f"Popped right: {popped_data}")
        return popped_data
    
    def print_deque(self):
        if self.head is None:
            print("Deque is empty!")
            return
        
        print("\n--- Deque Contents (Left to Right) ---")
        current = self.head
        position = 1
        
        while current is not None:
            print(f"{position}. {current.data}")
            current = current.next
            position += 1
        
        print(f"Total elements: {self.size}\n")

if __name__ == "__main__":
    deque = Deque()
    
    deque.push_right(10)   
    deque.push_right(20)   
    deque.push_left(5)    
    deque.push_left(1)     
    deque.push_right(30)   
    
    deque.print_deque()
    
    deque.pop_left()       
    deque.pop_right()      
    
    deque.print_deque()
    
    deque.push_left(0)     
    deque.push_right(25)   
    
    deque.print_deque()
    
    deque.pop_left()
    deque.pop_left()
    deque.pop_right()
    deque.pop_right()
    deque.pop_right()
    
    deque.print_deque()
    deque.pop_left()