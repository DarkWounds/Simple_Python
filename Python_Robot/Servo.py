
class Servo:
    def __init__(self, nume):
        this.nume = nume
        this.currPos = 0.0;
        
    def setPosition(self, position):
        this.currPos = range(-1, 1, position)
        
    def getPosition(self):
        return this.currPos
    
    def getName(self):
        return this.name
    
           
 