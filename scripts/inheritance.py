class Bolid:
    team = None
    formula_type = 1
    driver = None

    def __init__(self, team, driver):
        self.team = team
        self.driver = driver
    
    def get_data(self):
        return (self.team, self.formula_type, self.driver)
    

class McLarenBolid(Bolid):
    color = 'orange'
    engine_type = 'Mercedes'
    bolid_number = None

    def __init__(self, bolid_number, driver):
        super().__init__('McLaren', driver)
        self.bolid_number = bolid_number

    def get_data(self):
        parent_data = super().get_data()
        return (self.color, self.engine_type, self.bolid_number, parent_data)
    
class RedBullRacingBolid(Bolid):
    color = 'dark blue'
    engine_type = 'Honda'
    bolid_number = None

    def __init__(self, bolid_number, driver):
        super().__init__('Red Bull Racing', driver)
        self.bolid_number = bolid_number

    def get_data(self):
        parent_data = super().get_data()
        return (self.color, self.engine_type, self.bolid_number, parent_data)
    
bolid_NOR = McLarenBolid(4, 'Lando Norris')
print(bolid_NOR.get_data())

bolid_VER = RedBullRacingBolid('1', 'Max Verstappen')
print(bolid_VER.get_data())

    