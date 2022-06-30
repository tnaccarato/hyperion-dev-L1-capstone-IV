# ------------------------------------------------------------------------------
# Author: Tom Naccarato (tcarlnaccarato@gmail.com)
#
# inventory.py (c) 2022
#
# Description:  A stock-taking and inventory management program for Nike
#               warehouses that reads a text file and allows the user to
#               perform a range of functions on 'Shoe' objects generated from
#               the file. These functions include searching for a product by
#               code (search_shoe), determining the product with the lowest
#               quantity and restocking it (re_stock), determining the product
#               with the highest quantity (highest_qty) and calculating the
#               value of each item entry, based on the quantity and cost of
#               the item (value_per_item).

# Created:  16/06/2022, 17:05:50
#
# Modified: 30/06/2022, 01:56:12
# ------------------------------------------------------------------------------
# Imported Libraries
# ------------------------------------------------------------------------------
import re
import tabulate
import pandas
# ------------------------------------------------------------------------------
# Defining Classes and Functions
# ------------------------------------------------------------------------------


class Shoe():
    '''Defines the Shoe class with the attributes country, code, product, cost
    and quantity.'''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def __str__(self):
        '''Returns a string representation of the class.'''
        return f"""\
Country:  {self.country}
Code:     {self.code}
Product:  {self.product}
Cost:     {self.cost}
Quantity: {self.quantity}
"""

    def get_cost(self):
        '''Returns the cost of the shoe.'''
        return self.cost

    def get_quantity(self):
        '''Returns the quantity of the shoes.'''
        return self.quantity


def main_menu():
    '''Prints a menu of options for the inventory manager and gives
    different options which call various functions of the program.'''
    # Prints a greeting message the first time the program is run
    print("Welcome to the Nike inventory manager! What would you like to do?")
    # Creates an empty string for menu_selection so that it can be referred
    # to before input on first run
    menu_selection = ""
    # Displays a menu until the user enters quit
    while menu_selection != "q":
        # Reads data from inventory.txt every time the menu is shown
        read_shoes_data()
        # Prints a list of options for the menu
        print("""
re -  Read data from inventory.txt file and save it to an inventory list
a -   Add a new shoe to the inventory list
v -   View data about every shoe in the inventory list
rs -  Restock the lowest quantity shoe in the inventory list
s -   Search for a shoe by product code
vps - Show the value per shoe (cost*quantity) for each shoe in the inventory \
list
h -   Print an \'on sale\' notice for the product with the highest quantity
q -   Quit the program
""")
        # Asks the user for input for option they want
        menu_selection = input("Enter your selection here: ")\
            .lower().replace(" ", "")
        # If user enters re, calls the read_shoes_data function to store
        # inventory.txt as list
        if menu_selection == "re":
            read_shoes_data()
            print("inventory.txt read and saved to list successfully.")
        # If user enters a, allows user to add a new shoe to the inventory
        elif menu_selection == "a":
            capture_shoes()
        # If user enters v, prints a table with information about all shoes
        elif menu_selection == "v":
            view_all()
        # If user enters rs, restocks the lowest quantity shoe
        elif menu_selection == "rs":
            re_stock()
        # If user enters s, allows user to search for a shoe by product code
        elif menu_selection == "s":
            search_shoe()
        # If user enters vps, prints table of shoes information with
        # additional column for the value per shoe (cost*quantity)
        elif menu_selection == "vps":
            value_per_item()
        # If user enters h, prints a sale notice for the shoe with the highest
        # quantity
        elif menu_selection == "h":
            highest_qty()
        # If the user enters q, quits the program
        elif menu_selection == "q":
            print("Thank you for using the Nike inventory manager. Goodbye!")
            quit()
        else:
            # If the option the user entered was not recognised, prints an
            # error message and allows them to try again
            print(f"The option \"{menu_selection}\" you selected was not \
recognised, please try again.")
            continue


def read_shoes_data():
    '''Opens the inventory.txt file and constructs a shoe object
    for each line of the file, using a try: except: block for error handling,
    and then adds the object to the 'shoes' list.'''
    # Clears the shoes list each time function is run to refresh it every time
    # it is run
    shoes.clear()
    # Reads the shoe data from inventory.txt
    try:
        with open("inventory.txt", "r", encoding="utf-8") as shoes_data:
            # Skip the first (header) line of the text file (1)
            next(shoes_data)
            # For each line in the file, split into a list of words
            for line in shoes_data:
                shoe = line.replace("\n", "").split(",")
                # Constructs a 'Shoe' object for each line
                try:
                    shoe = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])
                    # Adds the shoe object to the 'shoes' list
                    shoes.append(shoe)
                # If an line was not formatted correctly, prints an error
                # message and quits the program
                except IndexError:
                    print("Sorry, an item in \"inventory.txt\" was not \
formatted correctly. Please ensure that each item is formatted in the \
following way : \"country,code,product,cost,quantity\" with no empty lines \
between products.")
                    quit()
    # If the file cannot be found, give an error message and exit the program
    except FileNotFoundError:
        print("Sorry, the inventory.txt file cannot be found. Please make \
that it is in the folder and restart the program.")
        quit()


def capture_shoes():
    '''Allows a user to capture data about a shoe and use it to create a
    shoe object, then append to the shoe list and adds it to the inventory.'''
    # Asks the user for different inputs for the attributes of the new shoe
    # stock
    country = input("Please enter the country this shoe is stocked in:\n")
    while True:
        try:
            code = input("Please enter the code of the product:\n").upper().\
                replace(" ", "")
            # If code is not the format "SKU" then 5 numbers (SKUXXXXX), raise
            # an error (2)
            if re.match(r"^SKU[0-9][0-9][0-9][0-9][0-9]\Z", code) is None:
                raise TypeError
        # If a TypeError is raised, asks user to try again
        except TypeError:
            print(f"The product code \"{code}\" you entered was not valid. \
Please ensure that your code is entered as follows and try again: \
\"SKUXXXXX\" where X's are digits from 0-9.")
            continue
        else:
            break
    product = input("Please enter the name of the product:\n")
    # Loops until user enters a valid response (3)
    while True:
        try:
            cost = float(input("Please enter the cost of the product, omitting\
 the currency:\n").replace(" ", ""))
        # If the user enters anything other than a number, give an error
        # message and let them try again.
        except ValueError:
            print("You can only enter a number. Please remember to omit the \
currency symbol and try again.")
            continue
        else:
            break
    while True:
        try:
            quantity = int(input("Please enter the quantity of this product in\
 stock:\n").replace(" ", ""))
        # If the user doesn't enter an integer, gives an error message and
        # lets them try again
        except ValueError:
            print("You can only enter a integer. Please try again.")
        else:
            break
    # Creates a shoe object from the inputs provided
    shoe = Shoe(country, code, product, cost, quantity)
    # Adds the new shoe to inventory.txt file
    with open("inventory.txt", "a", encoding="utf-8") as shoe_data:
        shoe_data.writelines(f"\n{country},{code},{product},{cost},{quantity}")
    # Adds the item to shoes list
    shoes.append(shoe)
    print("Shoe has been successfully added. Returning to menu.")


def view_all():
    '''Iterates through the shoes list, converts to a dictionary then pandas
    dataframe and displays all shoes in a table.'''
    # Calls the read_shoes_data function to reread the inventory.txt
    read_shoes_data()
    # Creates an empty list for storing shoe objects as dictionaries
    shoes_dict_list = []
    # For each shoe in the list, appends the dictionary of an object to the
    # list (4)
    for shoe in shoes:
        shoes_dict_list.append(shoe.__dict__)
    # Converts the dictionary to a dataframe (5)
    shoes_dataframe = pandas.DataFrame(shoes_dict_list)
    # Capitalises the first letter of each of the headers (6)
    shoes_dataframe.columns = map(str.capitalize, shoes_dataframe.columns)
    # Creates a table from the shoes dataframe (7) and prints it
    table = tabulate.tabulate(shoes_dataframe, headers="keys",
                              tablefmt="fancy_grid")
    print(table)


def find_lowest_stock():
    '''Finds the product with the lowest amount of stock from the shoes list'''
    # Creates an empty list for storing shoe quantities
    shoe_quantity = []
    # Iterates through the shoes list and adds the quantity to shoe_quantity
    # list
    for shoe in shoes:
        shoe_quantity.append(shoe.get_quantity())
    # Finds the lowest value in quantity list
    lowest_stock_quantity = min(shoe_quantity)
    # Finds the index of the lowest value stock and assigns it a global
    # variable
    for shoe in shoes:
        if lowest_stock_quantity == shoe.quantity:
            global lowest_stock_index
            lowest_stock_index = shoes.index(shoe)
    # Stores the product with the lowest quantity to a global variable
    global lowest_quantity_product
    lowest_quantity_product = shoes[lowest_stock_index]


def find_highest_stock():
    '''Finds the product with the highest amount of stock from the shoes
    list'''
    # Creates an empty list for storing shoe quantities
    shoe_quantity = []
    # Iterates through the shoes list and adds the quantity to shoe_quantity
    # list
    for shoe in shoes:
        shoe_quantity.append(shoe.get_quantity())
    # Finds the highest value in quantity list
    highest_stock_quantity = max(shoe_quantity)
    # Finds the index of the highest value stock and assigns it a global
    # variable
    for shoe in shoes:
        if highest_stock_quantity == shoe.quantity:
            global highest_stock_index
            highest_stock_index = shoes.index(shoe)
    # Stores the product with the highest quantity to a global variable
    global highest_quantity_product
    highest_quantity_product = shoes[highest_stock_index]


def re_stock():
    '''Restocks the product with the lowest quantity in the shoes list by an
amount given as input from the user, changing the value in both the list and
inventory.txt file.'''
    # Calls the find_lowest_stock function
    find_lowest_stock()
    # Prints a statement telling the user the product with the lowest stock and
    # ask if they want to restock it
    print(f"{lowest_quantity_product.product} has the least stock \
({lowest_quantity_product.quantity}). Would you like to restock it? (y/n)")
    restock_response = input("Enter your selection here:").lower()\
        .replace(" ", "")
    # If they answer y or yes, ask how much they want to restock
    if restock_response == "y" or restock_response == "yes":
        while True:
            try:
                restock_amount = int(input("Please enter the amount you \
would like to restock:"))
                # Adds the restock amount to the old stock
                new_stock = (lowest_quantity_product.quantity + restock_amount)
                shoes_data_string = ""
                # Opens the inventory.txt file
                with open("inventory.txt", "r", encoding="utf-8") as \
                        shoes_data:
                    # Writes shoes_data to a new string by line
                    for line in shoes_data:
                        shoes_data_string += line
                    # Splits the new string into a list of lines
                    shoes_data_string = shoes_data_string.split("\n")
                    # Creates a variable for the shoe to restock with the index
                    # of the lowest quantity shoe
                    restocked_shoe = shoes_data_string[lowest_stock_index + 1]
                    # Splits the restocked shoe into a list of words
                    restocked_shoe = restocked_shoe.split(",")
                    # Replaces the quantity of the lowest quantity shoe with
                    # the new quantity after restock
                    restocked_shoe[4] = str(new_stock)
                    # Joins the restocked shoe list back together
                    restocked_shoe = ",".join(restocked_shoe)
                    # Replaces the line in the string of shoe data with the
                    # restocked shoe amount
                    shoes_data_string[lowest_stock_index + 1] = restocked_shoe
                    # Rejoins the shoes_data string so that it can be written
                    # to file
                    shoes_data_string = "\n".join(shoes_data_string)
                # Writes the shoes_data_string to file
                with open("inventory.txt", "w", encoding="utf-8") as \
                        shoes_data:
                    shoes_data.writelines(shoes_data_string)
                # Prints a confirmation
                print(f"{lowest_quantity_product.product} has been \
successfully restocked. New stock is {new_stock}.")
            # If the user doesn't enter an integer, allows them to try
            # again
            except ValueError:
                print("You can only enter an integer. Please try again.")
                continue
            else:
                break
    # If the user enters n or no, returns to menu
    elif restock_response == "n" or restock_response == "no":
        print("Returning to menu...")
    # Otherwise, gives an error message and allows the user to try again.
    else:
        print("Response not recognised. Please try again.")
        re_stock()


def search_shoe():
    '''Takes the product code of a shoe as input and prints the details for the
    shoe found.'''
    # Assigns a None variable to searched_shoe
    searched_shoe = None
    # Takes input from the user for the product code of the shoe they want to
    # search
    while True:
        try:
            shoe_search = input("Please enter the product code of the shoe \
you would like to search: ").upper().replace(" ", "")
            # If code is not the format "SKU" then 5 numbers (SKUXXXXX), raise
            # an error
            if re.match(r"^SKU[0-9][0-9][0-9][0-9][0-9]\Z", shoe_search) is \
                    None:
                raise TypeError
        # If a TypeError is raised, asks user to try again
        except TypeError:
            print(f"The product code \"{shoe_search}\" you entered was not \
valid. Please ensure that your code is entered as follows and try again: \
\"SKUXXXXX\" where X's are digits from 0-9.")
            continue
        else:
            break
    # Searches the list of shoes for a shoe with that product code
    for shoe in shoes:
        # If a match for the product code is found, assigns it to the
        # searched_shoe variable
        if shoe.code == shoe_search:
            searched_shoe = shoe
    # If no match is found, searched shoe will remain None and so
    # prints an error message and allows the user to try again
    if searched_shoe is None:
        print(f"Sorry, a shoe with the product code {shoe_search} could \
not be found. Please try again.")
        search_shoe()
    # Otherwise, prints the __str__ information for that shoe
    else:
        print(searched_shoe)


def value_per_item():
    '''Takes the value and the quantity of each item and calculates the value
    per item by multiplying them together,
    then prints the information in a new table.'''
    for shoe in shoes:
        # Calculates the value per shoe by multiplying the cost and the
        # quantity together
        value_per_shoe = shoe.get_cost() * shoe.get_quantity()
        # Assigns a new attribute to the shoe with the value per shoe
        shoe.value_per_item = value_per_shoe
    # Creates an empty list for storing shoe objects as dictionaries
    shoes_dict_list = []
    # For each shoe in the list, appends the dictionary of an object to the
    # lists
    for shoe in shoes:
        shoes_dict_list.append(shoe.__dict__)
    # Converts the dictionary to a dataframe
    shoes_dataframe = pandas.DataFrame(shoes_dict_list)
    # Capitalises the first letter of each of the headers
    shoes_dataframe.columns = map(str.capitalize, shoes_dataframe.columns)
    # Creates a table from the shoes dataframe and prints it
    table = tabulate.tabulate(shoes_dataframe, headers="keys",
                              tablefmt="fancy_grid")
    print(table)


def highest_qty():
    '''Finds the shoe with the highest quantity and prints that it is for
    sale.'''
    # Calls the function to find the highest stock
    find_highest_stock()
    # Prints a notice saying the highest quantity shoe is for sale
    print(f"{highest_quantity_product.product}s on sale now!!! Get 'em fast\
, only {highest_quantity_product.get_quantity()} left in stock!")
# ------------------------------------------------------------------------------


# Creates an empty list for shoe objects
shoes = []

# Calls the main menu function
main_menu()

# ------------------------------------------------------------------------------
# References
# ------------------------------------------------------------------------------
# (1) Used info from here on skipping the header line of a text file:
# https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row
#
# (2) Used info from here on regular expression:
# https://docs.python.org/3/library/re.html
#
# (3) Used info from here on looping input until correct:
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#
# (4) Used info from here on how to use __dict__ function:
# https://www.tutorialspoint.com/What-does-built-in-class-attribute-dict-do-in-Python
#
# (5) Used info from here on how to convert a dictionary into a dataframe:
# https://stackoverflow.com/questions/55482252/printing-dict-as-tabular-data
#
# (6) Used info from here on formatting headers in a dataframe:
# https://stackoverflow.com/questions/19726029/how-can-i-make-pandas-dataframe-column-headers-all-lowercase
#
# (7) Used info from here on how to use the tabulate module:
# https://pypi.org/project/tabulate/
# ------------------------------------------------------------------------------
