import unittest

class calculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(2+1, 3,'Should be 3')
        
    def test_subtraction(self):
        self.assertEqual(4-2, 2,'should be 2')
        
    def test_multiplication(self):
        self.assertEqual(3*2, 6,'should be 6')

    def test_division(self):
        self.assertEqual(6/2, 3,'should be 3')

if __name__ == "__main__":
    unittest.main()