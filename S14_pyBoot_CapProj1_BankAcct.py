#Sample Capstone Project
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/12-Final%20Capstone%20Python%20Project/02-Final%20Capstone%20Project%20Ideas.ipynb
#
'''
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/12-Final%20Capstone%20Python%20Project/03-Final%20Capstone%20Suggested%20Walkthrough.ipynb
Final Capstone Project - Suggested Walkthrough:
This is a suggested method for handling one of the Final Capstone Projects. We start by coding out the strictest requirements, and then build out from a working baseline model. Feel free to adapt this solution, and add features you think could help. Good luck!

Bank Account Manager
Under the Classes section in the list of suggested final capstone projects is a Bank Account Manager program. The goal is to create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Then you should manage credits and debits from these accounts through an ATM style program.

Project Scope
To tackle this project, first consider what has to happen.

There will be three different types of bank account (Checking, Savings, Business)
Each account will accept deposits and withdrawals, and will need to report balances
Project Wishlist
We might consider additional features, like:
-impose a monthly maintenance fee
-waive fees for minimum combined deposit balances
-each account may have additional properties unique to that account:
-Checking allows unlimited transactions, and may keep track of printed checks
-Savings limits the number of withdrawals per period, and may earn interest
-Business may impose transaction fees
-automatically transfer the "change" for debit card purchases from Checking to Savings,
 where "change" is the amount needed to raise a debit to the nearest whole dollar
-permit savings autodraft overdraft protection

Let's get started!

Step 1: Establish an abstract Account class with features shared by all accounts.
Note that abstract classes are never instantiated, they simply provide a base class with attributes and methods to be inherited by any derived class.
Step 2: Establish a Checking Account class that inherits from Account, and adds Checking-specific traits.
Step 3: TEST setting up a Checking Account object
Step 4: Set up similar Savings and Business account classes
Step 5: Create a Customer class
For this next phase, let's set up a Customer class that holds a customer's name and PIN and can contain any number and/or combination of Account objects.
Step 6: TEST setting up a Customer, adding accounts, and checking balances
Step 7: Let's write some functions for making deposits and withdrawals.¶
Be sure to include a docstring that explains what's expected by the function!
'''