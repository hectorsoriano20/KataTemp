import unittest
import temp

class Testtemp(unittest.TestCase):
    def test_C_2_F(self):
        self.assertEqual(temp.C_2_F(20), 68.0)

    def test_C_2_K(self):
        self.assertEqual(temp.C_2_K(20), 293.15)
        
    def test_F_2_C(self):
        self.assertEqual(temp.F_2_C(92), 33.333333333333336)
        
    def test_F_2_K(self):
        self.assertEqual(temp.F_2_K(92), 306.4833333333333)
        
    def test_K_2_F(self):
        self.assertEqual(temp.K_2_F(450), 350.33)
        
    def test_K_2_C(self):
        self.assertEqual(temp.K_2_C(450), 176.85000000000002)
    
if __name__ == "__main__":
    unittest.main()