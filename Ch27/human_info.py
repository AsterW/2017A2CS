from library_items_info import *


class Borrower:
    def __init__(self, name, email):
        self.borrowerName = name
        self.emailAddress = email
        self.borrowerID = LibraryItem.getBorrowerID(self)
        self.itemsOnLoan = 0

    def getBorrowerName(self):
        return self.borrowerName

    def getEmailAddress(self):
        return self.emailAddress

    def getBorrowerID(self):
        return self.borrowerID

    def getItemsOnLoan(self):
        return self.itemsOnLoan

    def updateItemsOnLoan(self):
        self.itemsOnLoan += 1

    def printDetails(self):
        print(self.borrowerName, "; ", self.emailAddress, "; ", end="")
        print(self.borrowerID, "; ", self.itemsOnLoan)