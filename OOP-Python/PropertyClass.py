# Code for understanding property in python using class

# https://www.programiz.com/python-programming/property

class Celsius:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def get_temp(self):
        print("Getting value...")
        return self._temperature

    def set_temp(self, temperature):
        print("Setting value...")
        if(temperature < -273.15):
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = temperature

    #temperature = property(get_temp, set_temp)
    #below three lines are equivalent to above line
    temperature = property()
    temperature = temperature.getter(get_temp)
    temperature = temperature.setter(set_temp)


    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

myTemperature = Celsius(40)

print(myTemperature.temperature)
print(myTemperature._temperature)
print(myTemperature.to_fahrenheit())



