import unittest

def text_reversed(text):
    return text[::-1]


class TestTextReversed(unittest.TestCase):
  
    def test_example_from_exercise(self):
      
        test_text = "Hola mundo"
    
        result = text_reversed(test_text)
        
        self.assertEqual(result, "odnum aloH")
    
    def test_simple_string(self):
        
        test_text = "Hello world"
        
        result = text_reversed(test_text)
        
        self.assertEqual(result, "dlrow olleH")
    
    def test_string_with_numbers_and_symbols(self):
      
        test_text = "Python123!"
        
        result = text_reversed(test_text)
        
        self.assertEqual(result, "!321nohtyP")

if __name__ == '__main__':
    unittest.main(verbosity=2)

