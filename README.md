```python
#  Coffee Shop CLI

A comprehensive command-line interface application for managing a coffee shop's customer orders, built with Python and SQLAlchemy. This system allows customer registration, menu browsing, order placement, and order history tracking.

## Features

- **Customer Management**: Register new customers and select existing ones
- **Menu Browsing**: View available coffee items with descriptions and prices
- **Order Processing**: Place orders with automatic total calculation
- **Order History**: View individual customer order history
- **Admin View**: See all orders across all customers
- **Database Persistence**: SQLite database with proper ORM modeling

## Project Structure
coffee_shop_cli/
├── models.py # SQLAlchemy database models
├── helpers.py # Database operations and utility functions
├── cli.py # Main command-line interface
├── requirements.txt # Python dependencies
└── coffee_shop.db # SQLite database (auto-created)

text

##  Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone and navigate to the project**:
   ```bash
   git clone <your-repo-url>
   cd coffee-shop-cli
Install dependencies:

bash
pip install -r requirements.txt
Run the application:

bash
python cli.py
 User Guide
Starting the Application
bash
python cli.py
You'll see the main menu:

text
--- Coffee Shop CLI ---
1. View menu
2. Register customer
3. Select customer
4. Place order (No customer selected)
5. View order history
6. View all orders
7. Exit
Step-by-Step Usage
1. View the Menu
bash
Choose option: 1
Displays all available coffee items with their descriptions.

2. Register as a New Customer
bash
Choose option: 2
Enter your name: John Doe
Enter your email: john@example.com
Registers a new customer. The system checks for duplicate emails.

3. Select an Existing Customer
bash
Choose option: 3
Enter customer email: john@example.com
Sets the current customer for ordering. You'll see: Hello John Doe!

4. Place an Order (Requires Customer Selection)
bash
Choose option: 4
Shows available menu items and prompts for:

Menu item ID

Quantity

Automatically calculates total and creates the order.

5. View Your Order History
bash
Choose option: 5
Shows all orders for the currently selected customer with detailed breakdown.

6. View All Orders (Admin View)
bash
Choose option: 6
Displays all orders from all customers with customer names and order status.

7. Exit the Application
bash
Choose option: 7
Gracefully closes the database connection and exits.

Sample Workflow
bash
$ python cli.py

--- Coffee Shop CLI ---
1. View menu
2. Register customer
3. Select customer
4. Place order (No customer selected)
5. View order history
6. View all orders
7. Exit

Choose option: 1

---Menu---
1. Espresso
   Strong black coffee
2. Latte
   Coffee with steamed milk
3. Cappuccino
   Espresso with foamed milk

Choose option: 2
Enter your name: Alice Smith
Enter your email: alice@example.com
Customer Alice Smith created!

Choose option: 4

Available menu items:
1. Espresso - $3.50
2. Latte - $4.50
3. Cappuccino - $4.00

Enter menu item ID: 2
Enter quantity: 2
Order placed successfully! Total: $9.00

Choose option: 5

Order history for Alice Smith:
Order #1 - $9.00 - 2023-12-07 14:30:25
  2x Latte @ $4.50

Choose option: 7
Thank you for visiting our coffee shop!
Data Model
The application uses these main entities:

Customer: Store customer information (name, email)

MenuItem: Coffee drinks with name, description, and price

Order: Customer orders with total amount and timestamp

OrderItem: Individual items within orders with quantity and price snapshot

Database Operations
Key Functions in helpers.py:
get_all_menu_items() - Retrieve all available coffee items

create_customer(name, email) - Register new customer

find_customer_by_email(email) - Find customer by email

create_order(customer_id, total_amount) - Create new order

create_order_item(order_id, menu_item_id, quantity, price) - Add items to order

get_customer_orders(customer_id) - Get order history for customer

get_all_orders() - Get all orders (admin view)

get_order_items(order_id) - Get items for specific order

 Development
Setting Up Development Environment
Install development dependencies:

bash
pip install sqlalchemy
Database initialization (handled automatically on first run)

Testing the application:

bash
python cli.py
Adding New Menu Items
Edit the database or modify the helpers.py file to include additional menu items with their descriptions and prices.

 Troubleshooting
Database connection issues:

Ensure SQLite is available

Check file permissions for database creation

Module not found errors:

Ensure all files are in the same directory

Check Python path

Duplicate email errors:

The system prevents duplicate customer registrations

 Future Enhancements
Potential features to add:

Payment processing simulation

Inventory management

Order status updates (preparing, ready, completed)

Customer loyalty program

Advanced reporting and analytics

Web interface integration


```