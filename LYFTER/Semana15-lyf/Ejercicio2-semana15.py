def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            
            if list_to_sort[j] < list_to_sort[j - 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j - 1]
                list_to_sort[j - 1] = temp

my_test_list = [64, 34, 25, 12, 22, 11, 90]

print("List before sorting:", my_test_list)

bubble_sort(my_test_list)

print("List after sorting:", my_test_list)