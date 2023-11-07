import unittest
from math_quiz import random_number_fun, random_number_fun, random_math_process


class TestMathGame(unittest.TestCase):

    def test_random_number_fun(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_fun(min_val, max_val) #get random number between minimum and maximum entered numbers
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_number_fun(self):
        # Test if random mathematical symbolegenerated  is correct
        for _ in range(1000):  # Test a large number of random values
            rand_symbole = random_number_fun() #get random number
            self.assertTrue(rand_symbole == "+" or rand_symbole == "-" or  rand_symbole == "*" )
    

    def test_random_math_process(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (6, 4, '-','6-1',5), (2, 3, '*', '2*3', 6), (60, 90, '+', '60+90', 150)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases: # check the test cases if they are right or not in the code
                if operator == "+":  
                     self.assertTrue(expected_answer = num1 + num2)
                elif operator == '-': 
                     self.assertTrue(expected_answer = num1 - num2)
                else operator == '*': 
                     self.assertTrue(expected_answer = num1 * num2)

                    
    

if __name__ == "__main__":
    unittest.main()
    
