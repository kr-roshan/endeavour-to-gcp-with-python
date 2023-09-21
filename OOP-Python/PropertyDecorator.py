# code to understand property in python using Decorator

# https://www.programiz.com/python-programming/property


'''

The @property Decorator
In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:

property(fget=None, fset=None, fdel=None, doc=None)
Here,

fget is function to get value of the attribute
fset is function to set value of the attribute
fdel is function to delete the attribute
doc is a string (like a comment)

'''

class Temperature:
    def __init__(self, temperatureInCelsius = 0):
        self.temperatureInCelsius = temperatureInCelsius
    
    @property
    def fahrenheit(self):
        return (self.temperatureInCelsius * 1.8) + 32
    
    @property
    def temperatureInCelsius(self):
        print("Getting value ...")
        return self._temperatureInCelsius

    @temperatureInCelsius.setter
    def temperatureInCelsius(self, value):
        print("Setting value...")
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperatureInCelsius = value
    
myTemperature = Temperature()
myTemperature.temperatureInCelsius = 41

print(myTemperature.fahrenheit)
print(myTemperature.temperatureInCelsius)

