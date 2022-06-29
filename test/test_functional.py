import unittest
from method_override import Sub
from single_inh import B
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_result_type(self):
        test_obj = TestUtils()
        obj=Sub()
        result=obj.calculate(5,4)
        if type(result)==type(1):
            test_obj.yakshaAssert("TestResultType", True, "functional")
            print("TestResultType = Passed")
        else:
            test_obj.yakshaAssert("TestResultType", False, "functional")
            print("TestResultType = Failed")
    def test_result(self):
        test_obj = TestUtils()
        obj=Sub()
        result=obj.calculate(5,4)
        if result==20:
            test_obj.yakshaAssert("TestResult", True, "functional")
            print("TestResult = Passed")
        else:
            test_obj.yakshaAssert("TestResult", False, "functional")
            print("TestResult = Failed")

    def test_instance_of_Sub(self):
        test_obj = TestUtils()
        obj=Sub()
        if isinstance(obj,Sub):
            test_obj.yakshaAssert("TestInstanceOfSub", True, "functional")
            print("TestInstanceOfSub = Passed")
        else:
            test_obj.yakshaAssert("TestInstanceOfSub", False, "functional")
            print("TestInstanceOfSub = Failed")

    def test_instance(self):
        test_obj = TestUtils()
        obj=B(2,5)
        if isinstance(obj,B):
            test_obj.yakshaAssert("TestInstance", True, "functional")
            print("TestInstance = Passed")
        else:
            test_obj.yakshaAssert("TestInstance", False, "functional")
            print("TestInstance = Failed")

    def test_calculate_power(self):
        test_obj = TestUtils()
        obj=B(2,5)
        result=obj.calculate_power()
        if result==32:
            test_obj.yakshaAssert("TestCalculatePower", True, "functional")
            print("TestCalculatePower = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatePower", False, "functional")
            print("TestCalculatePower = Failed")
