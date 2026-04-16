from enum import Enum

class RunMode(Enum):
    RUN_WITHOUT_ENCODER = 1
    RUN_WITH_ENCODER = 2
    RUN_TO_POSITION = 3

class Motor:
    
    def __init__(self, nume, max_rpm):  # constructor
        self.nume = nume                # self = this din Java
        self.max_rpm = max_rpm
        self.current_rpm = 0
        self.runMode = RunMode.RUN_WITHOUT_ENCODER # variabila de clasa

    def set_power(self, power):
        power = max(-1, min(1, power))  # asigurăm că power este între -1 și 1
        self.current_rpm = power * self.max_rpm

    def get_rpm(self):
        if(self.runMode == RunMode.RUN_WITH_ENCODER):
            return self.current_rpm
        return 0
    
    def set_run_mode(self, mode):
        self.runMode = mode
        
    def get_run_mode(self):
        return self.runMode
    
    def set_position(self, position):
        if(self.runMode == RunMode.RUN_TO_POSITION):
            self.current_rpm = position * self.max_rpm / 100
            
    def get_position(self):
        if(self.runMode == RunMode.RUN_TO_POSITION):
            return self.current_rpm * 100 / self.max_rpm
        return 0
    
                
motor1 = Motor("Shooter", 6000)
motor1.set_run_mode(RunMode.RUN_WITH_ENCODER)
motor1.set_power(0.8)
print(f"RPM: {motor1.get_rpm()}")

motor2 = Motor("Intake", 435)
print(f"RunMode: {motor2.get_run_mode().name}")