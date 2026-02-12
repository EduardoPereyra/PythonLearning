import unittest

def is_prime_number(number:int) -> bool:
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

class Test(unittest.TestCase):
    def test_number_equal_or_less_than_one(self):
        number = 1
        result = is_prime_number(number)
        self.assertFalse(result)
    
    def test_prime_number_false(self):
        number = 4
        result = is_prime_number(number)
        self.assertEqual(False, result)
        self.assertFalse(result)
    
    def test_prime_number_true(self):
        number = 3
        result = is_prime_number(number) 
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()