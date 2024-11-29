class Member:
    def __init__(self, id, sex, height : list, weight : list):
        self.id = id
        self.sex = sex
        self.height = height
        self.weight = weight
        
    def calc_bmi(self):
        return self.weight[-1] / (self.height[-1] * self.height[-1])

    def return_value(self):
        return_value = ""
        for i in range(len(self.height)):
            return_value += f"{self.height[i]},{self.weight[i]}\n"
        return return_value
    
    
    