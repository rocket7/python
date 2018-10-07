import pytz
import datetime

class Account:
    """
    Comments for class
    MUST Use SELF prefix
    """

    # STATIC CLASS - SHARED BY ALL MEMBERS OF CLASS
    # Use Leading _underscore as indicator this should be considered "private" to class
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)



    def __init__(self, name, initial_dep):
        self._name = name
        self.__balance = 0
        self.transaction_list = [] # Initialize LIST
        self.deposit(initial_dep)
        print("Account created for " + self._name)


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))
        else:
            print("The amount deposited must be greater than zero")


    def withdrawl(self, amount):
        if amount > 0:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                self.transaction_list.append((Account._current_time(), -amount))
            else:
                print("The amount must be greater than zero and no more than your balance available")
            self.show_balance()


    def show_balance(self):
        print("Balance is {}".format(self.__balance))


    def show_transactions(self):
        for date, amount in self.transaction_list:  # UNPACKS TUPLE AND ASSIGNS VALUES AT SAME TIME
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


#
# MAIN PART OF APPLICATION
#

if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.show_balance()
    tim.withdrawl(100)
    tim.show_balance()
    tim.withdrawl(12)
    tim.show_balance()
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.show_balance()
    steph.deposit(90)
    steph.show_balance()
    steph.withdrawl(2)
    steph.show_balance()
    steph.show_transactions()
    steph.__balance = 200 # CREATES AS NEW ATTRIBUTE - ORIGINAL IS '_Account__balance'
    print(steph.__dict__)

