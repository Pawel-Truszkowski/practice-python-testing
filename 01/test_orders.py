import unittest
from orders import validate_order

class TestValidateOrder(unittest.TestCase):
   def test_return_true_when_valid_data_order(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "courier",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      result = validate_order(order)
      self.assertTrue(result)
   
   def test_return_true_when_delivery_method_is_courier(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "courier",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      result = validate_order(order)
      self.assertTrue(result)
   
   def test_return_true_when_delivery_method_is_pickup(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "pickup",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      result = validate_order(order)
      self.assertTrue(result)
    
   def test_return_true_when_delivery_method_is_drone(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         "delivery": {
            "method": "drone",         
            "address": "ul. Polna 10, 00-001 Warszawa"
            }
         }
      result = validate_order(order)
      self.assertTrue(result)
 
   def test_incorrect_user_id(self):
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
   
   def test_raises_key_error_when_lack_of_delivery_in_structure(self):
      order = {
         "user_id": 10,
         "items": ["keyboard", "mouse", "monitor"],
         }
      with self.assertRaises(KeyError) as context:
         validate_order(order)
   

if __name__ == "__main__":
    unittest.main()
