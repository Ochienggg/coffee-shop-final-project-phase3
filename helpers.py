from .models import session, Customer, MenuItem, Order, OrderIte

def seed_database():
    # Create sample customers
    customers = [
        Customer(name="John Doe", email="john@example.com"),
        Customer(name="Jane Smith", email="jane@example.com"),
        Customer(name="Bob Johnson", email="bob@example.com")
    ]
    
    # Create sample menu items
    menu_items = [
        MenuItem(
            name="Espresso",
            description="Strong black coffee made by forcing steam through ground coffee beans",
            price=2.50,
            category="Hot Coffee"
        ),
        MenuItem(
            name="Cappuccino",
            description="Espresso with steamed milk and a deep layer of foam",
            price=3.50,
            category="Hot Coffee"
        ),