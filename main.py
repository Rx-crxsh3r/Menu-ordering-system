from rich.console import Console

availability = True
A_availablility = True
fees = 0
A_Fees = 0
A_Total = 0

class UserInterface:    
    menu = r'''
APPETIZERS
burgers,
pasta,
noodles,
fries,
ADD-ONS
cake,
coffee,
water,
dressing'''
    
    def __init__(self):
        self.console = Console()

    def print_ascii_art(self):
        self.console.print("Welcome to our humble restaurant, what appetizer would you like to order?", justify="center", style="#D3869B bold")
        print("\n")
        self.Todays_menu()
    
    def Todays_menu(self):
        self.console.print("Today's menu: ", justify="full", style="#D3869B")
        self.console.print(self.menu, justify="center", style="#D3869B")

    def print_receipt_A(self, x, y, z):
        self.console.print(f"The total fees to be paid are: {z}", justify="center", style="#D3869B")
        self.console.print(f"The fees for the appetizer(s) are: {x}", justify="center", style="#D3869B")
        self.console.print(f"The fees for the add-on(s) for the appetizer are: {y}", justify="center", style="#D3869B")

    def waiting_time(self):
        self.console.print("Your order will arrive in 12 minutes", justify="center", style="#D3869B")

def A_appetizer(x, y):
    if x > 0:
        extra = input("Would you like a drink or an add-on with that? ")
        if extra.lower() in ("yes", "y"):
            addons = input("What would you like as an addon? ")
            addonslst = addons.strip().split(", ")
            for addon in addonslst:
                if addon.lower() == "cake":
                    y += 12
                elif addon.lower() == "coffee":
                    y += 3
                elif addon.lower() == "water":
                    y += 2
                elif addon.lower() == "dressing":
                    y += 4
                elif addon.lower() in ("nothing", "no"):
                    pass
                else:
                    print("One or more of the add-on(s) you entered is not available in today's menu, please view the menu and try again.")
                    ui.Todays_menu()
                    return A_appetizer(x, y)
            return y
    else:
        print("You can't order an add-on to an APPETIZER without an appetizer")
    return y

def appetizer(x):
    order = input("Enter order: ")
    orderlst = order.strip().split(", ")
    for item in orderlst:
        if item.lower() in ("burgers", "burger"):
            x += 13
        elif item.lower() == "fries":
            x += 5
        elif item.lower() == "pasta":
            x += 9
        elif item.lower() == "noodles":
            x += 5
        elif item.lower() == "nothing":
            pass
        else:
            print("One or more of the items you entered is not available in today's menu, please view the menu and try again.")
            ui.Todays_menu()
            return appetizer(x)
    return x

ui = UserInterface()
ui.print_ascii_art()
fees = appetizer(fees)

A_Fees = A_appetizer(fees, A_Fees)

if fees > 0 and A_Fees >= 0:
    A_Total = fees + A_Fees
    ui.print_receipt_A(fees, A_Fees, A_Total)
    ui.waiting_time()
else:
    print("Invalid order or no order placed.")
