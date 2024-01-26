
class Purchase:
    invoices = {}
    def __init__(self, invoice_number, sales_amount, num_of_items):
        self.invoice_number = invoice_number
        self.sales_amount = sales_amount
        self.num_of_items = num_of_items
        self.sales_tax_rate = 0.05
        self.shipping_charges = 0
        self.calculate_sales_tax()
        self.calculate_shipping_charges()

    def calculate_sales_tax(self):
        self.sales_tax_amount = self.sales_amount * self.sales_tax_rate

    def calculate_shipping_charges(self):
        if self.num_of_items < 3:
            self.shipping_charges = 3.50
        elif 3 <= self.num_of_items <= 6:
            self.shipping_charges = 5.00
        elif 7 <= self.num_of_items <= 10:
            self.shipping_charges = 7.00
        else:
            self.shipping_charges = 10.00

    def __str__(self):
        total_amount = self.sales_amount + self.sales_tax_amount + self.shipping_charges
        return f"Purchase# {self.invoice_number} details\nInvoice number: {self.invoice_number}\n" \
               f"Sales amount: ${self.sales_amount:.2f}\nSales tax : {int(self.sales_tax_rate * 100)}%\n" \
               f"Sales tax amount : ${self.sales_tax_amount:.2f}\nShipping charges : ${self.shipping_charges:.2f}\n" \
               f"Total amount : ${total_amount:.2f}"

    @staticmethod
    def validate_invoice_number(invoice_number):
        return 1000 <= invoice_number <= 9000

def enter_invoice():
    while True:
        invoice_number = int(input("Enter a invoice number between 1000 and 9000 : "))
        if not Purchase.validate_invoice_number(invoice_number):
            print("Invalid data entered for invoice")
            continue
        sales_amount = float(input("Enter the sales amount: "))
        while sales_amount < 0:
            print("Invalid data entered for sales amount, Please enter a nonnegative value.")
            sales_amount = float(input("Enter the sales amount: "))
        num_of_items = int(input("Enter number of items purchased: "))
        return Purchase(invoice_number, sales_amount, num_of_items)

def view_invoices():
    invoice_number = int(input("Enter a valid number between 1000 and 9000 : "))
    if Purchase.validate_invoice_number(invoice_number):
        if invoice_number in Purchase.invoices:
            print(Purchase.invoices[invoice_number])
        else:
            print("Invalid invoice number. Invoice does not exist.")
    else:
        print("Invalid invoice number. Please enter a valid invoice number between 1000 and 9000.")

def manage_invoice():
    invoice_number = int(input("Enter a valid number between 1000 and 9000 : "))
    if Purchase.validate_invoice_number(invoice_number):
        if invoice_number in Purchase.invoices:
            print(f"\n###### Managing Purchase# {invoice_number} ######")
            print("1. Update the purchase details.")
            print("2. Delete the purchase order.")
            print("3. Get back to the main menu.")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                update_invoice(invoice_number)
            elif choice == 2:
                delete_invoice(invoice_number)
        else:
            print("Invalid invoice number. Invoice does not exist.")
    else:
        print("Invalid invoice number. Please enter a valid invoice number between 1000 and 9000.")

def update_invoice(invoice_number):
    purchase = Purchase.invoices[invoice_number]
    sales_amount = float(input("Enter the updated sales amount: ") or purchase.sales_amount)
    num_of_items = int(input("Enter the updated number of items purchased: ") or purchase.num_of_items)
    Purchase.invoices[invoice_number] = Purchase(invoice_number, sales_amount, num_of_items)
    print(f"\n##### Purchase# {invoice_number} Updated #####\n")

def delete_invoice(invoice_number):
    confirmation = input(f"Are you sure you want to delete Purchase# {invoice_number}. (Y/N)? ").upper()
    if confirmation == 'Y':
        del Purchase.invoices[invoice_number]
        print(f"\n##### Purchase# {invoice_number} Deleted #####\n")

def main_menu():
    while True:
        print("\n###### MAIN MENU ######")
        print("1. Enter a new Invoice")
        print("2. View list of Invoices")
        print("3. Manage an Invoice")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            purchase = enter_invoice()
            Purchase.invoices[purchase.invoice_number] = purchase
        elif choice == 2:
            view_invoices()
        elif choice == 3:
            manage_invoice()
        elif choice == 4:
            save_to_file()
            print("Exit.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")


def save_to_file():
    with open("./data/assignment.txt", "w") as file:
        for purchase in Purchase.invoices.values():
            file.write(str(purchase) + "\n")


if __name__ == "__main__":
    while True:
        main_menu()