import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    # def test_something(self):
    #    self.assertEquals(False, True)

    def test_monthFunction(self):
        x = 4
        result = camper_age_input.convert_to_months(x)
        self.assertEquals(result, 48)


if __name__ == '__main__':
    unittest.main()
