class Bolid:
    team = None
    driver = None
    max_speed = None

    def set_data(self, team, driver, max_speed):
        self.team = team
        self.driver = driver
        self.max_speed = max_speed

    def get_data(self):
        return(self.team, self.driver, self.max_speed)
    

mclarenNor = Bolid()
mclarenNor.set_data('McLaren', 'Lando Norris', 345)

print(mclarenNor.get_data())

redbullVer = Bolid()
redbullVer.set_data('Red Bull Racing', 'Max Verstappen', 350)

print(redbullVer.get_data())