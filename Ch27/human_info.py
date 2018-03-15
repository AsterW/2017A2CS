
class Borrower:
    def __init__(self, name, email, borrowerID):
        self.borrowerName = name
        self.emailAddress = email
        self.borrowerID = borrowerID
        self.itemsOnLoan = 0

    def getBorrowerName(self):
        return self.borrowerName

    def getEmailAddress(self):
        return self.emailAddress

    def getBorrowerID(self):
        return self.borrowerID

    def getItemsOnLoan(self):
        return self.itemsOnLoan

    def updateItemsOnLoan(self, n):
        self.itemsOnLoan += n

    def printDetails(self):
        print(self.borrowerName, "; ", self.emailAddress, "; ", end="")
        print(self.borrowerID, "; ", self.itemsOnLoan)