class Member:
    def __init__(self, name, sex, weight, height):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        
    def calc_bmi(self):
        return self.weight / (self.height * self.height)

    def retrun_string(self):
        return f"{self.name}|{self.sex}|{self.weight}|{self.height} "
    