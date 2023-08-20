class parentClass:
    def __init__(self):
        self.name = "Nagaraj"
        self.location = "Hyderabad"
        self.pincode = 516004
    def method1(self):
        return f"{self.name} located at {self.location}"
class childClass(parentClass):
    def __init__(self):
        super.__init__()