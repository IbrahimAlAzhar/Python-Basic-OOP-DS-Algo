import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase): # create a class which inherit from unititest.TestCase
    """Tests for a 'name_function.py' """

    def test_first_last_name(self): # the method should start with 'test' word
        """test which have not a middle name,Do name like 'Ibrahim Al Azhar' work ?"""
        formatted_name = get_formatted_name('ibrahim','al azhar')
        self.assertEqual(formatted_name,'Ibrahim Al Azhar') # check the formatted name which is using get_formatted_name function,assert methods verify that a result you received matches the result you expected to receive
    def test_first_last_middle(self):
        """"test names like which has middle name"""
        formatted_name = get_formatted_name('ibrahim','al','azhar')
        self.assertEqual(formatted_name,'Ibrahim Al Azhar')

unittest.main()