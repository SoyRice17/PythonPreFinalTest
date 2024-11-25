class Member:
    def __init__(self, id, sex, height, weight):
        self.id = id
        self.sex = sex
        self.height = height
        self.weight = weight
        
    def calc_bmi(self):
        return self.weight / (self.height * self.height)

    def retrun_string(self):
        return f"{self.id}|{self.sex}|{self.height}|{self.weight}"
    
    def __str__(self): # 테스트 코드 (필요한것 아님)
        return f"{self.id}|{self.sex}|{self.height}|{self.weight} "
    
    