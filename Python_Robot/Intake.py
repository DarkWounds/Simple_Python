from enum import Enum
from Python_Robot.ButtonEX import ButtonEX
from Motor import Motor

class Intake:
    
    motorIntake = Motor("IntakeMotor", 100)
    butonFront = ButtonEX("FrontButton")
    butonBack = ButtonEX("BackButton")
    state = Enum('FRONT', 'STOP', 'BACK')
    inState = state.STOP
    
    def __init__(self): 
        pass
    
    