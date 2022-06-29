
import unittest
from method_override import Sub
from single_inh import B
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_on_calculate_power(self):
        test_obj = TestUtils()
        try:
            obj=B('2',5)
            obj.calculate_power()
            test_obj.yakshaAssert("TestTypeErrorOnCalculatePower", False, "exception")
            print("TestTypeErrorOnCalculatePower= Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnCalculatePower", True, "exception")
            print("TestTypeErrorOnCalculatePower = Passed")

    def test_type_error_on_calculate(self):
        test_obj = TestUtils()
        try:
            obj=Sub()
            obj.calculate(5)
            test_obj.yakshaAssert("TestTypeErrorOnCalculate", False, "exception")
            print("TestTypeErrorOnCalculate = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnCalculate", True, "exception")
            print("TestTypeErrorOnCalculate = Passed")
