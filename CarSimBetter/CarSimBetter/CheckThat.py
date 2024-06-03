import time

class CheckThat(object):
    
    def __init__(self):
        self.RIGHT = 1
        self.LEFT = -1
        self.FORWARD = 1
        self.REVERSE = 0
        
    def isWrongGear(self, selectedGear, speed):
        
        if (selectedGear == self.REVERSE and speed > 0) or (selectedGear == self.FORWARD and speed < 0):
            print("BOOM!")
            return True 
        else:
            return False
    
    def isInForwardReverse(self, selectedGear, speed):  
     #if the car is stopped. either place in forward or reverse
     if speed == 0:
        if selectedGear == self.FORWARD:
           print('Car is in FORWARD...')
           time.sleep(1)
           return self.FORWARD
        
        else:
           print("car is in REVERSE")
           return self.REVERSE
     else:
        return selectedGear
    
    def isAcceleratingForwardReverse(self, gear, speed):
     
     if gear >= self.FORWARD:
        speed +=5
        
     elif gear == self.REVERSE:
        speed -=5
     return speed
 
    def isTopSpeedForwardReverse(self, speed):
     if speed > 80:
       speed = 80
       print("You are at Max Speed!")
       time.sleep(1)
     elif speed < -10:
        speed = -10
        print("You are at Max Speed!")
     return speed
 
    def isBrakingForwardReverse(self, gear, speed):
     # Braking Forward 
     if gear >= self.FORWARD:
       if speed >= self.FORWARD:
          speed -= 5
          print("Braking...")
          time.sleep(1)
          return
       else:
        print("Car is stopped.")
     # Braking Reverse    
     elif gear == self.REVERSE:
        if speed < self.REVERSE:
          self.speed += 5
          print("Braking...")
          time.sleep(1)
          
        else:
          print("Car is stopped.")
     return speed
           
    def isItAclock(self, direction):
     if direction == 13:
        direction = 1
        
     elif direction == 0:
        direction = 12
        
     return direction
    
    def isTurningInReverse(self, gear, direction_change):
     if self.gear == self.REVERSE: # checking to see if car is in reverse
        direction_change *= -1
        
        if direction_change == self.RIGHT:
            print('Turning Left...')
            
        else:
            print('Turning Right...')
            
     return direction_change    
    
    def isTurning(self, direction_change):
     if direction_change == self.RIGHT:
            print('Turning Right...')
            time.sleep(1)
     elif direction_change == self.LEFT:
            print('Turning Left...')
            time.sleep(1)
     




