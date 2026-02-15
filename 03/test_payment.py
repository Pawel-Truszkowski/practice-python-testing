from unittest.mock import Mock
from payment import send_payment
import pytest

def test_successful_payment():
   mock_gateway = Mock()
   mock_gateway.pay.return_value = True
   
   payment_data = {
      "amount": 100, 
      "currency": "PLN"
   }
   result = send_payment(payment_data=payment_data, gateway=mock_gateway)
   
   assert result is True
   mock_gateway.pay.assert_called_once_with(payment_data)
   
def test_payment_exception():
   mock_gateway = Mock()
   mock_gateway.side_effect = Exception("Payment failed!")
   
   result = send_payment({}, gateway=mock_gateway)
   
   assert result is False
   
   
   
