from hoge import my_add, my_sub

def test_hoge():
  actual = my_add(2,3)
  expected = 5
  assert expected == actual
  actual = my_sub(2,3)
  expected = -1
  assert expected == actual
  
  
