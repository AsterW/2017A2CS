import pickle
class carRecord():
    def __init__(self):
        self.vehicleID = ""
        self.registration = ""
        self.dateofRegistration = None
        self.engineSize = 0
        self.purchasePrice = 0.00
        self.vehicleNum = ""

class carList():
    def __init__(self):
        self.records = []
        for i in range (5):
            thisCar = carRecord()
            thisCar.vehicleNum = i + 1
            self.records.append(thisCar)

carList = []
thisCar = carRecord()
thisCar.vehicleID = "001"
thisCar.registration = "LA"
thisCar.dateofRegistration = 2.26
thisCar.engineSize = 1
thisCar.purchasePrice = 14.00
carList.append(thisCar)

thisCar = carRecord()
thisCar.vehicleID = "002"
thisCar.registration = "SF"
thisCar.dateofRegistration = 2.27
thisCar.engineSize = 2
thisCar.purchasePrice = 15.00
carList.append(thisCar)

thisCar = carRecord()
thisCar.vehicleID = "003"
thisCar.registration = "STL"
thisCar.dateofRegistration = 2.28
thisCar.engineSize = 3
thisCar.purchasePrice = 16.00
carList.append(thisCar)

thisCar = carRecord()
thisCar.vehicleID = "004"
thisCar.registration = "WAS"
thisCar.dateofRegistration = 2.29
thisCar.engineSize = 4
thisCar.purchasePrice = 17.00
carList.append(thisCar)

thisCar = carRecord()
thisCar.vehicleID = "005"
thisCar.registration = "NYC"
thisCar.dateofRegistration = 3.01
thisCar.engineSize = 5
thisCar.purchasePrice = 18.00
carList.append(thisCar)

carFile = open("Cars.DAT", "wb")
for i in range (5):
    pickle.dump(carList[i], carFile)

carFile.close()

carFile = open("Cars.DAT", "rb")
carList2 = []
for i in range (5):
    carList2.append(pickle.load(carFile))

carFile.close()

for i in range (5):
    print("vehicleID:", carList2[i].vehicleID, "registration:", carList2[i].registration, "date of registration:",
          carList2[i].dateofRegistration, "engineSize:", carList2[i].engineSize, "purchasePrice",
          carList2[i].purchasePrice)