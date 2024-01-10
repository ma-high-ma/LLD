class CartStatus:
    ACTIVE = "active"
    ARCHIVED = "archived"
    PURCHASED = "purchased"

class InventoryActivity:
    ADD = "add"
    REMOVE = "remove"

class OrderStatus:
    SHIPPED = "shipped"
    PENDING = "pending"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class PaymentStatus:
    SUCCESSFUL = "successful"
    FAILED = "failed"
