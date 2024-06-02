

import time



RIGHT = 1
LEFT = -1
FORWARD = 1
REVERSE = 0

class Car:
  def __init__(self):
        self.speed = 0
        self.gear = 1
        self.direction = 0
        self.broken = False  # indicates whether car is broken
        self.simulation = []
        self.simulation_loaded = False
        
 ######## CHECKS ##########
  def isBroken(self):
     if self.broken:
      print("Car is Broken!!!")
      return
  
  def isWrongGear(self, selected_gear):
     if (selected_gear == REVERSE and self.speed > 0) or (selected_gear == FORWARD and self.speed < 0):
        self.broken = True
        print("BOOM!")
        return
     
  def isInForward(self, seleted_gear):   
     if self.speed == 0:  # And self.speed is 0...
        self.gear = FORWARD  # Change gear to 1
        print('Car is in FORWARD...')
        time.sleep(1)
        return True
     else:
        return False
     
  def isInReverse(self, selected_gear):
     if selected_gear == REVERSE: 
        self.gear = REVERSE 
        print('Car is in REVERSE.')
        time.sleep(1)
        return
     
   # if the car is in 1st or higher gear, it accelerates forward.     
  def isTravelingForward(self):
     if self.gear >= FORWARD:
        self.speed +=5
        self.change_gear()
        return
        
   # if the car is in reverse, it accelaerates backward.     
  def isTravellingInReverse(self):
      if self.gear == REVERSE:
       self.speed -= 5
       self.change_gear()
       return
      
  # if the car is at max speed it will not let is accelerate higher.
  def isTopSpeedForward(self):
     if self.speed >80:
       self.speed = 80
       print("You are at Max Speed!")
       time.sleep(1)
       return
     
  # does the same in reverse.
  def isTopSpeedReverse(self):
     if self.speed < -10:
       self.speed = -10
       print("you are at Max Speed in Reverse!")
       time.sleep(1)
       return
   
   
 # Slows forward motion by 5km/h, if the car is stopped it tells the user.
  def isBrakingForward(self):
     if self.gear >= FORWARD:
       if self.speed >=FORWARD:
          self.speed -= 5
          print("Braking...")
          time.sleep(1)
          return
       else:
        print("Car is stopped.")
        return 
  
    # does the same in reverse.
  def isBrakingInReverse(self):
     if self.gear == REVERSE:
       if self.speed < REVERSE:
          self.speed += 5
          print("Braking...")
          time.sleep(1)
          return
       else:
          print("Car is stopped.")
          return
  # checks that the turning circle remains a clock. 
  def isItAclock(self):
     if self.direction == 13:
        self.direction = 1
        return
     elif self.direction == 0:
        self.direction = 12
        return
     
  def isTurningInReverse(self, direction_change):
     if self.gear == REVERSE: # checking to see if car is in reverse
        direction_change *= -1
        
        if direction_change == RIGHT:
            print('Turning Left...')
            
        else:
            print('Turning Right...')
            
     return direction_change
  
  def isTurning(self, direction_change):
     if direction_change == RIGHT:
            print('Turning Right...')
            time.sleep(1)
     elif direction_change == LEFT:
            print('Turning Left...')
            time.sleep(1)
  
     
###### FUNTIONALITY #######
     
  def accelerate(self):
    self.isBroken()
    time.sleep(1)
    print("Accelerating...")
  # checks whether to accelerate forward or backward.
    self.isTravelingForward()
    self.isTravellingInReverse()
   # checks that car does not exceed max speed in both directions.  
    self.isTopSpeedForward()
    self.isTopSpeedReverse()
    return
  
   
  def brake(self):
     self.isBroken()
   # checks whether to brake forwards or backwards     
     self.isBrakingInReverse()
     self.isBrakingForward()
     self.change_gear()
     return
  


  def turn_steering_wheel(self, directionChange):
    self.isBroken()
    print("Turning...")
    self.isTurningInReverse(directionChange)
    self.isTurning(directionChange)
    self.direction += directionChange
    self.isItAclock()
    return

  def change_gear(self, selectedGear = FORWARD):
     
     self.isBroken
     self.isWrongGear(selectedGear)
     isForward = self.isInForward(selectedGear)
     self.isInReverse(selectedGear)
     
     if self.gear > 0:
        gear_ratio = [5, 10, 15, 20, 25, 30, 35, 40, 45]
        gears_avail = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        
        for index in range(0, len(gears_avail)):
           if self.speed == gear_ratio[index] and gears_avail[index] != self.gear:
              self.gear = gears_avail[index]
              print("Changing gear...")
              time.sleep(1)
              
     
 
  def display_stats(self):
      print(f"Speed = {self.speed} Gear = {self.gear}  Direction = {self.direction} \n")
      time.sleep(1)
 

  def load_simulation(self, filename):
     try:
        openFile = open(filename)
        fileData = openFile.read()
        self.simulation = fileData.split('\n')
        openFile.close()
        print("Loading Simulation...")
        self.simulation_loaded = True
        
     except IOError as NoFileFound:
        print("There is no file associated with this simulator.")
        


 
  def run_simulation(self):
     
     # dictionary with all recognised commands and actions.
     commands_and_actions = {
        "FORWARD": (self.change_gear, FORWARD),     
        "ACCELERATE": (self.accelerate, None), 
        "LEFT": (self.turn_steering_wheel, LEFT), 
        "RIGHT": (self.turn_steering_wheel, RIGHT), 
        "BRAKE": (self.brake, None),           
        "REVERSE": (self.change_gear, REVERSE)
        }
     

     # executes action via dictionary.
     for command in self.simulation:
        action = commands_and_actions.get(command)
        if action:
           method, arg = action
           if arg is not None:
              method(arg)
           else:
              method()
              self.display_stats()
        else:
           print("This command is not recognised.")
           
        
  


if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
