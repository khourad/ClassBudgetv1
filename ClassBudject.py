
class Budget:
    def __init__(self, name):
        self.name = name
        self.record = [

        ]

    def deposit(self, amount, note):
        """
        A deposit method accepts an amount and note
        amount:int. It adds money into your budget balance
        note:str. It adds the name of what amount is deposited for
        it appends a list into a record in the format; [amount, note]
        """

        self.record.append([amount, "Deposited for " + note])


    def withdrawal(self, amount, note):
        """
        A withdrawal method similar to the deposit method.
        amount:int. It subtracts money from the budget balance and should be stored as a negative number
        note:str. it adds a note to describe what amount is withdrawn for
        if there are not enough funds, nothing should be added to the record.
        This method should return True if the withdrawal took place, and False otherwise.
        """

        if (self.checkFunds(amount)):
            self.record.append([amount, "Withdrawn for " + note])
            return True
        return False


    def showBalance(self):
        """ 
        A showBalance method that returns the current balance of the budget category based on the deposit 
        and withdrawals made
        """

        total = 0
        for item in self.record:
            total += item[0]

        return total

    def transfer(self, amount, category):
        """
        A Transfer method that accepts an amount and another budget category as arguments.
        the method should add a withdrawal with the amount and note " Transfer to [Destination Budget Category]"
        The method should then add a depoisit to the other budget category with the amount and note 
        "Transfer from [Source budget category]
        If there are not enough funds, nothing should be added to either record.
        This method should return True if the transfer took place, and False otherwise.
        """
        
        if (self.checkFunds(amount)):
            self.withdrawal(amount, "Transfer to " + category.name)
            category.depoisit(amount, "Transfer from " +self.name)
            return True
        return False


    def checkFunds(self, amount):
        """
        A checkFunds method that accepts an amount as an argument. It returns False if the amount is greater than 
        the balance of the budget category and returns True otherwise. This method should be used by both the withdrawal
        and transfer method.
        """

        if(self.showBalance() >= amount):
            return True
        return False

        
        

    def printRecord(self):

        return self.record