print("***** Welcome to Shopping Cart *****")
# Initializing an empty list to store products
p = []

# Asking the user if they want to start a cart
cart = input("Insert cart (y/n): ")
if cart == "y":
    # Infinite loop to keep the shopping process running
    while True:
        # Displaying the menu options
        print("Select type:\n\t1. Add items\n\t2. Display cart\n\t3. Checkout.")
        # Taking user input for the choice
        data = int(input("Enter choice: "))
        
        # If the user chooses to add items
        if data == 1:
            # Taking product details as input from the user
            pid = int(input("Enter product id: "))
            pname = input("Enter product name: ")
            price = float(input("Enter product price: "))
            qty = int(input("Enter product quantity: "))
            # Calculating total price for the product
            total_price = price * qty
            # Creating a list of the product details
            product = [pid, pname, price, qty, total_price]
            # Adding the product to the cart
            p.append(product)
            print("Product added successfully")
        
        # If the user chooses to display the cart
        elif data == 2:
            # Looping through each product in the cart
            for i in p:
                # Looping through each detail of the product
                for j in i:
                    # Printing the product details
                    print(j, end=" ")
                print()  # New line for each product
        
        # If the user chooses to checkout
        elif data == 3:
            # Calculating the total amount of the cart
            total_amount = sum(item[4] for item in p)
            # Checking if the total amount is eligible for a discount
            if total_amount >= 2000:
                # Calculating discount and delivery charges
                discount = total_amount * 0.10
                delivery = 0
                paid_amount = total_amount - discount + delivery
            else:
                # If not eligible for discount, setting discount to 0 and adding delivery charges
                discount = 0
                delivery = 40
                paid_amount = total_amount - discount + delivery
            # Printing the billing details
            print("Total amount:\t", total_amount)
            print("Discount:\t", discount)
            print("Delivery:\t", delivery)
            print("Paid amount:\t", paid_amount)
        
        # Asking the user if they want to exit the cart
        ex = input("Do you want to exit (y/n): ")
        # Breaking the loop if the user wants to exit
        if ex == "y":
            break
else:
    # Printing an error message if the cart is not started
    print("Invalid cart")