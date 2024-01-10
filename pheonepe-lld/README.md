Assumptions


User
Products
Product Inventory

User -> n Cart -> n Cart Item -> product , quantity

User -> Order -> Cart

Cart Item
id, cart_id, product_id, quantity

Product Inventory
product, qty

quantity < 0

user -> order -> []
