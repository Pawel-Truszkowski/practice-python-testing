import unittest
from orders import validate_order

class TestValidateOrder(unittest.TestCase):
   def test_if_user_id_is_correct(self):
      order = {
         "user_id": "",
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "courier",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      with self.assertRaises(ValueError) as context:
         validate_order(order)
      
      self.assertEqual(str(context.exception), "Nieprawidłowy user_id")

   
   

if __name__ == "__main__":
    unittest.main()
