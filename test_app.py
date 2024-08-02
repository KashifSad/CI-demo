import unittest
from app import add,sub,mul

class TestMathFunctions(unittest.TestCase):
    def testadd(self):
        self.assertEqual(add(4,9), 13)
        self.assertEqual(add(-1,1), 0)


    def testsub(self):
        self.assertEqual(sub(7,3), 4)
        self.assertEqual(sub(9,7),2)

    def testmul(self):
        self.assertEqual(mul(2,7),14)
        self.assertEqual(mul(9,9), 81)

if __name__ == '__main__':
    unittest.main()