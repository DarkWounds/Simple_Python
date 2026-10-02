class Servo:
    
    nume = ""
    currPos = 0.0
    
    def __init__(self, nume):
        self.nume = nume
        self.currPos = 0.0;
        
    def setPosition(self, position):
        self.currPos = range(-1, 1, position)
        
    def getPosition(self):
        return self.currPos
    
    def getName(self):
        return self.nume
    
           
 