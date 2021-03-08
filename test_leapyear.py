import unittest
import leapyear


class TestCase(unittest.TestCase):
    def test_leapyear1(self):
        self.assertEqual(leapyear.leap(400),True)
    def test_leapyear2(self):
        self.assertEqual(leapyear.leap(117),False)
    def test_leapyear3(self):
        self.assertEqual(leapyear.leap(200),False)
    def test_leapyear4(self):
        self.assertEqual(leapyear.leap(2020),True)
    def test_leapyear5(self):
        self.assertEqual(leapyear.leap(2000),True)
    def test_leapyear6(self):
        self.assertEqual(leapyear.leap(2021),False)
    def test_leapyear7(self):
        self.assertEqual(leapyear.leap("Pit"),None)

if __name__ == "__main__":
    unittest.main(verbosity=2)
