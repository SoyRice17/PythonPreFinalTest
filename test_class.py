class Member:
    def __init__(self, id, sex, weight, height):
        self.id = id
        self.sex = sex
        self.weight = weight
        self.height = height
        
    def calc_bmi(self):
        return self.weight / (self.height * self.height)

    def retrun_string(self):
        return f"{self.id}|{self.sex}|{self.weight}|{self.height} "
    