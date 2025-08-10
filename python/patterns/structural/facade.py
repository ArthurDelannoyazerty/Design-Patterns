
class InventorySystem:
    def check_stock(self, product_id: str) -> bool:
        print(f"InventorySystem: Checking stock for product '{product_id}'...")
        return True

class PaymentGateway:
    def process_payment(self, customer_id: str, amount: float) -> bool:
        print(f"PaymentGateway: Processing payment of ${amount} for customer '{customer_id}'...")
        return True

class ShippingService:
    def schedule_shipping(self, order_id: str, address: str):
        print(f"ShippingService: Scheduling shipping for order '{order_id}' to '{address}'...")
        return "TRACK-XYZ-987"

class OrderFacade:
    """The Facade"""
    def __init__(self):
        self._inventory = InventorySystem()
        self._payment = PaymentGateway()
        self._shipping = ShippingService()

    def place_order(self, product_id: str, customer_id: str, amount: float, address: str) -> bool:
        print("\n--- OrderFacade: Initiating order placement ---")
        if not self._inventory.check_stock(product_id):
            print("OrderFacade: Order failed, product is out of stock.")
            return False
        
        if not self._payment.process_payment(customer_id, amount):
            print("OrderFacade: Order failed, payment was not successful.")
            return False
            
        tracking_number = self._shipping.schedule_shipping(
            order_id=f"ORD-{product_id}-{customer_id}",
            address=address
        )
        
        print(f"OrderFacade: Order placed successfully! Tracking number: {tracking_number}")
        print("------------------------------------------")
        return True


# ---------------------------------------------------------------------------- #
#                                  Client/Main                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    order_facade = OrderFacade()

    success = order_facade.place_order(
        product_id="PROD-123",
        customer_id="CUST-A4B5",
        amount=99.99,
        address="123 Main St, Anytown, USA"
    )

    if success:
        print("\nClient: Yay! My order was placed successfully.")
    else:
        print("\nClient: Oops! Something went wrong with my order.")

# ---------------------------------- Output ---------------------------------- #

# --- OrderFacade: Initiating order placement ---
# InventorySystem: Checking stock for product 'PROD-123'...
# PaymentGateway: Processing payment of $99.99 for customer 'CUST-A4B5'...
# ShippingService: Scheduling shipping for order 'ORD-PROD-123-CUST-A4B5' to '123 Main St, Anytown, USA'...
# OrderFacade: Order placed successfully! Tracking number: TRACK-XYZ-987
# ------------------------------------------
# 
# Client: Yay! My order was placed successfully.