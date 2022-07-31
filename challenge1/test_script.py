import unittest
from script import getValue

class CheckgetValue (unittest.TestCase): 

    def test_positive(self):  
  
        data = '{"x":{"y":{"z":{"a":"1"}}}}' 
        key = "x/y/z/a"
        result = getValue(data,key)  
        self.assertEqual(result, '1')

    def test_invalid_object(self):  
        data = 'dummy' 
        key = "x/y"
        result = getValue(data,key)  
        self.assertEqual(result, 'Invalid object passed')

    def test_invalid_key(self):  
        data = '{"a":{"b":{"c":"d"}}}'
        key = "a/b/z"
        result = getValue(data,key)  
        self.assertEqual(result, 'Invalid key passed')
  