import unittest
import hoge

class TestMyApp(unittest.TestCase):
  def test(self):
    actual = hoge.my_add(2,3)
    expected = 5
    self.assertEqual(expected, actual)
    actual = hoge.my_sub(2,3)
    expected = 5
    self.assertEqual(expected, actual)
  
if __name__ == "__main__":
  unittest.main()
  
