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
   
   
   def test_items_in_orders_are_empty(self):
      order = {
         "user_id": 10,
         "items": [],
         "delivery": {
            "method": "courier",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      with self.assertRaises(ValueError) as context:
         validate_order(order)
      
      self.assertEqual(str(context.exception), "Pusta lista items")
    
      
   def test_incorrect_delivery_method(self):
      order = { 
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "test",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      with self.assertRaises(ValueError) as context:
         validate_order(order)
   
      self.assertEqual(str(context.exception), "Nieprawidłowy sposób dostawy")
               
   
   def test_empty_delivery_address(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "drone",         
            "address": ""
            }
         }
      with self.assertRaises(ValueError) as context:
         validate_order(order)
      
      self.assertEqual(str(context.exception), "Brak adresu")

   
   

if __name__ == "__main__":
    unittest.main()
