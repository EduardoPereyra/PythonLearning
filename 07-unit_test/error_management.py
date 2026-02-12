import unittest

def calculate_average_try_except(numbers:list[int]) -> float | None: 
    try: 
        average = sum(numbers) / len(numbers)
        return average
    except Exception as e:
        print(f"An error occurred: {e}") 
        return None
    
def calculate_average(numbers:list[int]):
    average = sum(numbers) / len(numbers)
    return average

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_try_except(self):
        list_of_numbers = [1, 2, 3, 4, 5]
        average_expected = 3.0
        average_result = calculate_average_try_except(list_of_numbers)
        self.assertEqual(average_expected, average_result)
        
    def test_calculate_average_try_except_empty_list(self):
        list_of_numbers:list[int] = [] 
        average_result = calculate_average_try_except(list_of_numbers) 
        self.assertIsNone(average_result)
        
    def test_calculate_average(self):
        list_of_numbers = [1, 2, 3, 4, 5]
        average_expected = 3.0
        average_result = calculate_average(list_of_numbers)
        self.assertEqual(average_expected, average_result)
        
    def test_calculate_average_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            list_of_numbers:list[int] = [] 
            calculate_average(list_of_numbers) 
        
if __name__ == "__main__":
    unittest.main()