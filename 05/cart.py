class Cart:
    def __init__(self):
        self._products = []
           
    def add(self, product):
        self._products.append(product)
    
    def remove(self, product):
        for index, value in enumerate(self._products):
            if value.get("name") == product:
                del self._products[index]
                return True
        return False
                
    def total(self):
        return sum(p['price'] for p in self._products)
      
    def items(self):
        return [product.copy() for product in self._products]
    

