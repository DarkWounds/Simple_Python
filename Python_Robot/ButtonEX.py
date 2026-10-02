class ButtonEX:
    buttonName = ""
    buttonState = False
    
    def __init__(self, buttonName):
        self.buttonName = buttonName
        self.buttonState = False
        
    def buttonpressed(self):
        return self.buttonState 