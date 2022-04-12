import unittest

class MytestCase (unittest.TestCase):
    def test_something (self):
        self.assertSetEqual(True, False)
if __name__ == '__main__':
    unittest.main()