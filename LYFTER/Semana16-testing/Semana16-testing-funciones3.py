import unittest

def ordersnakecase(text):
    
    words_list = text.split('-')
    words_list.sort()
    return '-'.join(words_list)


class TestOrderSnakeCase(unittest.TestCase):
    
    def test_example_from_exercise(self):
       
        test_text = "python-variable-funcion-computadora-monitor"
        
        result = ordersnakecase(test_text)
        
        self.assertEqual(result, "computadora-funcion-monitor-python-variable")
    
    def test_code_example(self):
      
        test_text = "computer-function-monitor-python-variable"
        
        result = ordersnakecase(test_text)
        
        self.assertEqual(result, "computer-function-monitor-python-variable")
    
    def test_short_word_list(self):
        
        test_text = "zebra-apple-banana"
        
        result = ordersnakecase(test_text)
        
        self.assertEqual(result, "apple-banana-zebra")

if __name__ == '__main__':
    unittest.main(verbosity=2)
