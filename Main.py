from ParkingLot import ParkingLot
import fileinput

for line in fileinput.input():

    '''here reading command one by one'''
    if 'create_parking_lot' in line:
       data = line.split()
       parkingLot=ParkingLot(int(data[1]))
    if 'park ' in line:
        data = line.split()
        slotflag = parkingLot.isSlotAvailable()
        if slotflag == True:
           slotNumber=parkingLot.getAvailableSlot()
           parkingLot.parkThePark(slotNumber,data[1],data[2])   
        else:
           print "Sorry, parking lot is full"
    if 'leave' in line:
        data = line.split()
        parkingLot.leaveTheCar(int(data[1]))
    if 'status' in line:
       parkingLot.showParkingStatus()
    if 'registration_numbers_for_cars_with_colour' in line:
       data = line.split()
       parkingLot.getRegistrationNumbersFoCarsWithColour(data[1])
    if 'slot_numbers_for_cars_with_colour' in line:
       data = line.split()
       parkingLot.getSlotNumbersForCarsWithColour(data[1])
    if 'slot_number_for_registration_number' in line:
       data = line.split()
       parkingLot.getSloNumberForRegistrationNumber(data[1])
