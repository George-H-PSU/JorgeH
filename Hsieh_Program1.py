#Hsieh_Program1
#Yuan-Chih Hsieh
#CMPSC132 Program1

class Car: 
    def __init__(self, _year_model, _make): 
        self._year_model = _year_model
        self._make = _make
        self._speed = 0 #assign 0 to the speed
    
    def accelerate(self):
        self._speed += 5 #plus 5 when this function is called
        return self._speed
    
    def brake(self):
        self._speed -= 5 #minus 5 when this function is called
        return self._speed
    
    def get_speed(self):
        return self._speed #return the speed value

def main():
    sample = Car('Tesla', '2020') #an instance for Car class
    for i in range(5): #accelerate 5 times and display current speed after each call
        sample.accelerate()
        print('Current speed:', sample.get_speed())
    for k in range(5): #brake 5 times and display current speed after each call
        sample.brake()
        print('Current speed:', sample.get_speed())

if __name__ == '__main__': main()