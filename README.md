# HyperionDev Capstone Project IV - OOP

A stock-taking and inventory management program for Nike warehouses that reads a text file and allows the user to perform a range of functions on 'Shoe' objects generated from  the file.

## Menu

The following menu is shown to the user:

re -  Read data from inventory.txt file and save it to an inventory list\
a -   Add a new shoe to the inventory list\
v -   View data about every shoe in the inventory list\
rs -  Restock the lowest quantity shoe in the inventory list\
s -   Search for a shoe by product code\
vps - Show the value per shoe (cost*quantity) for each shoe in the inventory
list\
h -   Print an \'on sale\' notice for the product with the highest quantity\
q -   Quit the program\

## Functions

### Read Shoe Data

If the user selects 're', the data from the inventory.txt file is read and iterated through to make a list of shoe objects.

### Capture Shoes

If the user selects 'a', allows the user to capture data about a shoe and creates a new
shoe object that is added to the inventory list and txt file.
The user is asked for the following data:

- Country
- Product Code - Must be entered as SKUXXXX, where Xs are digits from 0-9
- Product Name
- Cost
- Quantity

### View All

If the user selects 'v', the shoes list is iterated through and printed as a
tabulate table for ease of reading.

### Restock

If the user selects 'rs', allows the user to increase the amount of stock of the
lowest quantity shoe by a certain amount.

### Search

If the user selects 's', allows the user to search for a shoe by its product code.

### Value Per Shoe

If the user selects 'vps', allows the user to see the value per shoe, calculated
 by the following:

**Cost * quantity**

And displays it in an easy to read tabulate table.

### Highest Quantity Notice

If the user selects 'h', displays a message saying:

**[Name of Highest Quantity Product] on sale now!!! Get 'em fast, only**
**[Quantity of Shoe] left in stock!")**

### Quit

If the user selects 'q', quits the program.
