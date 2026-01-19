import unittest

def my_list(numbers):   
    return sum(numbers)


class TestMyList(unittest.TestCase):
   
    def test_positive_numbers(self):
      
        test_list = [5, 10, 10, 15]
        
        result = my_list(test_list)
        
        self.assertEqual(result, 40)
    
    def test_mixed_numbers(self):

        test_list = [10, -5, 20, -3]
        
        result = my_list(test_list)
       
        self.assertEqual(result, 22)
    
    def test_example_from_exercise(self):

        test_list = [4, 6, 2, 29]
        
        result = my_list(test_list)
        
        self.assertEqual(result, 41)

if __name__ == '__main__':
    unittest.main(verbosity=2)

