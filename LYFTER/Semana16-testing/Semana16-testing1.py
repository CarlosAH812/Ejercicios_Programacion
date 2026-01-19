import unittest
import random

def bubble_sort(list_to_sort):
    
    n = len(list_to_sort)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp


class TestBubbleSort(unittest.TestCase):
    
    def test_small_list(self):
    
        test_list = [64, 34, 25, 12, 22, 11, 90]
        
        bubble_sort(test_list)
        
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])
    
    def test_large_list(self):
        
        test_list = [random.randint(1, 1000) for _ in range(150)]
    
        expected_result = sorted(test_list)
        
        bubble_sort(test_list)

        self.assertEqual(test_list, expected_result)
    
    def test_empty_list(self):
    
        test_list = []
        
        bubble_sort(test_list)
        
        self.assertEqual(test_list, [])
    
    def test_non_list_parameter(self):
    
        with self.assertRaises((TypeError, AttributeError)):
            bubble_sort("not a list")
        
        with self.assertRaises((TypeError, AttributeError)):
            bubble_sort(42)
        
        with self.assertRaises((TypeError, AttributeError)):
            bubble_sort(None)

if __name__ == '__main__':
    unittest.main(verbosity=2)