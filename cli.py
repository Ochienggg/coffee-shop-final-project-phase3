from lib.helpers import *
from lib.models import session




def main_menu():
    current_customer = None

    while True:
        print("/n--- coffee Shop CLI ---")
        print("1. View menu")
        print("2. Register customer")
        print("3. Select customer")
        if current_customer:
            print(f"4. Place order ({current_customer.name})")
            print("5. View order history")
        print("6. View all orders")
        print("7. Exit")

        choice = input("Choose option:").strip()

        if choice =="1":
            menu_items = get_all_menu_items()
            if menu_items:
                print("\n---Menu---")
                for item in menu_items:
                    print(f"{item.id}. {item.name}")
                    print (f"{item.desciption}")
            else:
                print("No menu items found")
        elif choice== "2":
            name = input("Enter your name:").strip()
            email = input("Enter your email").strip()

            if find_customer_by_name(email):
                print("Email already registered!")

            else:
                current_customer = create_customer(name, email)
                print(f"Customer {name} created!")

        elif choice == "3":
            email = input("Enter customer email: ").strip()
            customer = find_customer_by_email(email)
            if customer:
                current_customer = customer
                print(f"Hello {current_customer.name}!")
            else:
                print("Customer not found")

        elif choice == "4" and current_customer:
            menu_items = get_all_menu_items()
            if not menu_items:
                print("No menu items available")
                continue
                
            print("\nAvailable menu items:")
            for item in menu_items:
                print(f"{item.id}. {item.name} - ${item.price}")       

            