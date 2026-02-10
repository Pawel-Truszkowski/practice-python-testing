
def validate_order(order): 
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    # uzupełnij resztę przypadków
    if not order.get("items"):
        raise ValueError("Pusta lista items")
    delivery_method = ("courier", "pickup", "drone")
    if order["delivery"]["method"] not in delivery_method:
        raise ValueError("Nieprawidłowy sposób dostawy")
    if not order["delivery"]["address"]:
        raise ValueError("Brak adresu")

    return True


if __name__ == "__main__":
    order = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "drone",         
        "address": "ul. Polna 10, 00-001 Warszawa"
        }
    }
    print(validate_order(order=order))