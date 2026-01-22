
def bubble_sort(list_to_sort):
    n = len(list_to_sort)  
    
    for i in range(n - 1):  
        
        for j in range(n - 1 - i):  
            
            if list_to_sort[j] > list_to_sort[j + 1]:  
                
                temp = list_to_sort[j]                   
                list_to_sort[j] = list_to_sort[j + 1]    
                list_to_sort[j + 1] = temp               

