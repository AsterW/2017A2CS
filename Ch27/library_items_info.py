# Andy Wang Task 27.02
import datetime
from human_info import *


class LibraryItem:
    def __init__(self, title, author, itemID):
        self.title = title
        self.author = author
        self.itemID = itemID
        self.onLoan = False
        self.dueDate = None
        self.borrowerID = None

    def getTitle(self):
        return self.title

    def getArthor(self):
        return self.author

    def getItemID(self):
        return self.itemID

    def getOnLoan(self):
        return self.onLoan

    def getDueDate(self):
        return self.dueDate

    def getBorrowerID(self):
        return self.borrowerID

    def borrowItem(self):
        self.onLoan = True
        self.dueDate = self.dueDate + datetime.timedelta(weeks = 3)
        self.borrowerID = self.getBorrowerID()

    def returnItem(self):
        self.onLoan = False

    def printDetails(self):
        print(self.title, "; ", self.author, "; ", end="")
        print(self.itemID, "; ", self.onLoan, "; ", self.dueDate, "; ", end="")


class Book(LibraryItem):
    def __init__(self, title, author, itemID):
        LibraryItem.__init__(self, title, author, itemID)
        self.isRequested = False
        self.requestedBy = 0

    def getIsRequested(self):
        return self.isRequested

    def setIsRequested(self):
        self.isRequested = True

    def printDetails(self):
        print("Book Details: ", end="")
        LibraryItem.printDetails(self)
        print(self.getIsRequested())


class CD(LibraryItem):
    def __init__(self, title, author, itemID):
        LibraryItem.__init__(self, title, author, itemID)
        self.genre = ""

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    def printDetails(self):
        LibraryItem.printDetails(self)
        print(self.genre)

thisBook = Book("And Justice For All", "Metallica", 1)
#thisCD.setGenre("Pop")
thisBook.printDetails()
