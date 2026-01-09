class Bolid:
    team = None
    driver = None
    max_speed = None

    def __init__(self, team = None, driver = None, max_speed = None):
        self.set_data(team, driver, max_speed)

    def set_data(self, team = None, driver = None, max_speed = None):
        self.team = team
        self.driver = driver
        self.max_speed = max_speed

    def get_data(self):
        return(self.team, self.driver, self.max_speed)
    

mclarenNor = Bolid('McLaren', 'Lando Norris', 345)
print(mclarenNor.get_data())

redbullVer = Bolid('Red Bull Racing', 'Max Verstappen', 350)
print(redbullVer.get_data())