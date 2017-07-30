class Ticket(object):
    '''
    This class is the parking ticket
    '''
    __slotId = 0
    __registratonNumber = None
    __color=None
    def __init__(self, slotId, registratonNumber,color):
        '''
        Constructor
        '''
        self.__slotId = slotId
        self.__registratonNumber = registratonNumber
        self.__color = color

    def getSlotId(self):
        '''
        The method to get the slot id
        '''
        return self.__slotId

    def getregistratonNumber(self):
        '''
        The method to get the registration number
        '''
        return self.__registratonNumber
    def getcolor(self):
        '''
        The method to get the car color
        '''
        return self.__color

    def setRegistratonNumber(self,registratonNumber):
        '''
        The method is to set the registration number
        '''
        self.__registratonNumber = registratonNumber

    def setColor(self,color):
        '''
        The method is to set the car color
        '''
        self.__color = color        
