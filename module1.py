import unittest

class MytestCase(unittest.TestCase):
    
    def test_case_one(self):
        self.assertTrue(100>99,'should be True')



    def test_two(self):
        self.assertEqual(40+60 , 100 ,'should be 100')   
    
    def test_three(self):
        self.assertGreater(10,5,'should be greater')
        
if __name__ == "__main__":
    unittest.main()