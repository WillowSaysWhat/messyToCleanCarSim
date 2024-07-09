# Messy To Cleaner Code: Car Simulator
Understanding how to write clean code has always eluded me. It is not something that is taught in any of my uni modules. While I am modulating and fucusing on the single-responsibility principle, I find myself lingering on whether I have found an acceptable outcome to my search for a template to follow.

## Messy Code Car Simulator
This is a novice project that was actually an assigment from year 0 (Foundaton) of my degree. This was the first challenge that I completed that was not in a Leetcode-style where test cases were available to check against. I was expected to create my own test cases. I competed this assignment with 7 months of Python classes and tutorials and 7 months of self-taught online learning through 3 certificates from edx website. Looking back, I can see that even after 14 months of learning to program, I still barely reached a beginner understanding of programming.

# The Car Simulator
The assessment was to design a simple Console car simulator. The code format was provided and looked like this:
```py
# Python
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
        self.broken = False 
        self.simulation = []
        self.simulation_loaded = False

   def accelerate(self):
       pass
   def brake(self):
       pass
   def turn_steering_wheel(self, direction_change):
       pass
  def change_gear(self, selected_gear = FORWARD):
      pass
  def display_stats(self):
      pass
  def load_simulation(self, filename):
      pass
  def run_simulation(self):
      pass

if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
```
The car sim was expected to react to commands read from a text file ``` simulation.txt ```. Example of the textfile below:
```txt
FORWARD
ACCELERATE
RIGHT
ACCELERATE
RIGHT
ACCELERATE
RIGHT
ACCELERATE
LEFT
ACCELERATE
LEFT
ACCELERATE
ACCELERATE
ACCELERATE
ACCELERATE
```
The car was thought of as Automatic, therefore, the user was not expected to interact with the sim to change gear. That was the simulations task.
The Automaic gear ratio was:
```py
gears change at (km/h) [5, 10, 15, 20, 25, 30, 35, 40, 45] 
gears numbered at      [1,  1,  2,  2,  3,  3,  4,  4,  5]
```
the 5th gear was used from 45km/h to the max speed of 80km/h
Every ACCELERATE command speeds the car up by 5km/h in either forward or reverse, depending on whether the car is in reverse or not.
A BRAKE command also slowed the car by 5km/h
The car's turning circle was represented by a clock face and the direction number correlated to 12-hour time. The sim started with the car facing 12 o'clock and a LEFT command would turn the car to 11 or a RIGHT command to 1.

### NOTE
I was schooled in Australia where we are firmly rooted in the metric system, Britain on the other hand introduced the metric system into education in the 1980 yet still seem to be confused whether they are an imperial or metic country. This means that my representation of km/h could in fact be mph. 
# Output
The text-based output was predetermined and was expected to look like this:
![image](https://github.com/WillowSaysWhat/messyToCleanCarSim/assets/126318401/3c60aebe-c84e-44bd-af48-afef542e3b42)


## Clean Code Car Simulator
This is the same project, but refactored after another 2 years of programming. I must point out that during this time, I did not programme in Python as C++ was our prinicle language. Using the concepts learned, I rewrote the project to reflect my ability as a student in their final year of study. 

## Changes made.
There were so many changes made, including simplification of conditionals, fixing code that repeats itself, minimising comments. Here is a more indepth look:

### Removing multiple if statements
I returned to this assessment a year or so after submission and the first things that frustated me was the amount of "if" statements in the run-simulator method. At the time I did not know how to improve this, however, the following year I was able to improve this by using a dictionary with a tuple as its value. The tuple contained the method and its argument to be passed. The dictionary key was the command, for example "ACCELERATE" or "BRAKE". This can be seen in the image below.

![ifStatements](https://github.com/WillowSaysWhat/messyToCleanCarSim/assets/126318401/9b92d32d-da03-4eeb-a283-cdcf422236f3)

### Minimising comments.
In my eagerness, I commented every line in my original assessment. I improved this by only commenting where necessary. This can be seen in the image above and below. I have learned over the years that over-commenting can make the code competely unreadable. This is, I believe the case with my original submission.

![changeGearBeforeAfter](https://github.com/WillowSaysWhat/messyToCleanCarSim/assets/126318401/b2e8079c-19e4-4827-9da5-bf2ffe19542c)


### Modulating Logic
It was the bloated methods that motivated me to refactor this project. The code was a "winding road" of logic with repeated code snippets and never ending lines of if statements. By moving the logic to another class and instantiating it in the Car class __init__ I was able to was able to code smaller and clearer methods. The above image demostrates the simplification of the ``` change_gear() ``` method. I named the logic class ``` checkThat ``` to make the code even more reader-friendly. 





