#import unittest
from hoge import my_add, my_sub

#class TestMyApp(unittest.TestCase):
  def test_hoge():
    actual = hoge.my_add(2,3)
    expected = 5
    assertEqual(expected, actual)
    actual = hoge.my_sub(2,3)
    expected = 5
    assertEqual(expected, actual)
  
#if __name__ == "__main__":
#  unittest.main()
  
