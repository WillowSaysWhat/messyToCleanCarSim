import time
from CheckThat import CheckThat

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
        self.checkThat = CheckThat() 
      
###### FUNTIONALITY #######
  # Checks whether car is broken.
  # checks whether car is accelerating forward or back by the gear it is in and then +/- 5.
  # does a gear change if needed.
  # Then checks to see if car is at max speed.
  def accelerate(self):
    
    if self.isBroken():
       return

    time.sleep(1)
    print("Accelerating...")
    self.speed = self.checkThat.isAcceleratingForwardReverse(self.gear, self.speed)
    self.change_gear()
    self.speed = self.checkThat.isTopSpeedForwardReverse(self.speed)
    return
  
  # Checks whether car is broken.
  # Checks whether car is braking traveling forward or reverse by gear and +/- 5km/h.
  # does a gear change if needed.
  def brake(self):
     
     if self.isBroken():
        return
     
     self.speed = self.checkThat.isBrakingForwardReverse(self.gear, self.speed)
     self.change_gear()
     return
  

  # checks whether car is broken.
  # prints direction turning.
  # turns car.
  # make sure we indicate direction with a clock.
  def turn_steering_wheel(self, directionChange):
    
    if self.isBroken:
        return
    
    print("Turning...")
    directionChange = self.checkThat.isTurningInReverse(self.gear, directionChange)
    self.checkThat.isTurning(directionChange)
    self.direction += directionChange
    self.checkThat.isItAclock(self.direction)
    return

  # checks that car is not suddenly being placed in opposing gear while traveling at speed. 
  # checks whether car is broken.
  # Checks whether the car is stopped and readly to be placed in gear.
  # changes gear using Lists and a loop.
  def change_gear(self, selectedGear = FORWARD):
     
     self.broken = self.checkThat.isWrongGear(selectedGear, self.speed)
     
     if self.isBroken:
        return
     
     self.gear = self.checkThat.isInForwardReverse(selectedGear, self.speed)  

     # Change gears
     if self.gear > 0:
        gear_ratio = [5, 10, 15, 20, 25, 30, 35, 40, 45]
        gears_avail = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        
        for index in range(0, len(gears_avail)):
           if self.speed == gear_ratio[index] and gears_avail[index] != self.gear:
              self.gear = gears_avail[index]
              print("Changing gear...")
              time.sleep(1)
              
     
  # displays data in console.
  def display_stats(self):
      print(f"Speed = {self.speed} Gear = {self.gear}  Direction = {self.direction} \n")
      time.sleep(1)
 
  # gets commands and places them in a List
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
        

  # finds command from the simulation List and matches it with 
  # commands_and_actions dictionary then executes the method and arg.
  def run_simulation(self):
     
     # this is an automatic transmition (D = FORWARD, R =REVERSE)
     commands_and_actions = {
        "FORWARD": (self.change_gear, FORWARD),     
        "ACCELERATE": (self.accelerate, None), 
        "LEFT": (self.turn_steering_wheel, LEFT), 
        "RIGHT": (self.turn_steering_wheel, RIGHT), 
        "BRAKE": (self.brake, None),           
        "REVERSE": (self.change_gear, REVERSE)
        }
     
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
          
# Execution
if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
