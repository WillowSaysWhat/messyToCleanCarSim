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

 ###### This method accelerates the car #######
    def accelerate(self):
        time.sleep(1)
        if self.broken: # check if car is broken – do nothing if it is
            print('Car is broken!!!')
            return

        print('Accelerating...')

        if self.gear >= FORWARD: # check ot see if we are in forward
            self.speed += 5 # modify speed (increase 5 miles an hour)
            self.change_gear()
        if self.gear == REVERSE:
            self.speed -= 5 # modify speed (increase 5 miles an hour)
        if self.speed > 80:# if speed greater than 80
            self.speed = 80 # speed is kept at 80
            print("You're doing 'Top Speed'!")
            time.sleep(1)
        if self.speed < -10: # if speed less than -10
            self.speed = -10 # speed is kept at -10
            print("You're doing 'Top Speed' in REVERSE!")
            time.sleep(1)

    ###### This method slows the car #######
    def brake(self):

        if self.broken: # check if car is broken – do nothing if it is
            print('Car is Broken!!!')
        elif self.gear == REVERSE: # if car is in reverse (0)
            if self.speed < REVERSE:
                self.speed += 5 # modify speed (increase 5 miles and hour)
                print('Breaking...')
                time.sleep(1)
            else:
                print('Car is stopped.')
                return
        elif self.gear >= FORWARD:# if gear is going forward (1-5)
            if self.speed >= FORWARD:
                self.speed -= 5 # modify speed (decrease 5 miles and hour)
                print('Breaking...')
                time.sleep(1)
                self.change_gear()
            else:
                print('Car is stopped.')
                return

    ###### This method tuers the car using "Clock Face" direction   #######
    def turn_steering_wheel(self, direction_change):

        if self.broken: # check to see if car is broken
            print('Car is broken!!!')
        elif self.gear == REVERSE: # checking to see if car is in reverse
            direction_change *= -1
            if direction_change == RIGHT:
                print('Turning Left...')
            else:
                print('Turning Right...')
        else: # if forward, just print which direction the car is turning
            if direction_change == RIGHT:
                print('Turning Right...')
                time.sleep(1)
            elif direction_change == LEFT:
                print('Turning Left...')
                time.sleep(1)
        # self. direction was changed to 12 in Load_simulation (line 173).
        self.direction = self.direction + direction_change # add direction_change to self.direction

        if self.direction == 13: # stops the value rising above 12 ( because its a clock)
            self.direction = 1 # changes 13 to 1

        elif self.direction == 0: # stops the value reching 0
                self.direction = 12 # change value to 12


    ###### This method changes the gear #######
    def change_gear(self, selected_gear= FORWARD):  # selected_gear is either FORWARD or REVERSE

        gear_ratio = [5, 10, 15, 20, 25, 30, 35, 40, 45]
        gears_avail = [1, 1, 2, 2, 3, 3, 4, 4, 5]

        if self.broken:  # check to see if car is broken
            print('Car is broken!!!')
            return
        elif selected_gear == REVERSE and self.speed > 0:  # if car is travelling in FORWARD and REVERSE is selected...
            self.broken = True  # The car breaks-down
            print('BOOM!')
        elif selected_gear == FORWARD and self.speed < 0:  # if car is travelling in REVERSE and FORWARD is selected...
            self.broken = True  # The car breaks-down
            print('BOOM!')

        elif selected_gear == FORWARD:  # if variable is FORWARD (1)
            if self.speed == 0:  # And self.speed is 0...
                self.gear = FORWARD  # Change gear to 1
                print('Car is in FORWARD...')
                time.sleep(1)

        elif selected_gear == REVERSE: # if Selected_gear is REVERSE
            self.gear = REVERSE # Change gear to REVERSE
            print('Car is in REVERSE.')
            time.sleep(1)

        if selected_gear == FORWARD: # if selected_gear is default ('FORWARD')

            for i in range(0, 9): # loop through a number range of 0 to 9
            # if car speed is in list(gear_ratio) and current gear is NOT in list(gears_avail)
                if self.speed == gear_ratio[i] and gears_avail[i] != self.gear:
                    self.gear = gears_avail[i] # change gear to list(gears_avail)[i]
                    print('changing gear...')
                    time.sleep(1)



    ###### This displays the data #######
    def display_stats(self):
        if self.broken:
            print('Car is broken!!!')
        else:
            # prints out the data for each attribute and then finishes with a new line.
            print(f"Speed = {self.speed} Gear = {self.gear}  Direction = {self.direction} \n")
            time.sleep(1)



    ###### This method loads the simulation #######
    def load_simulation(self, filename):
        # try/except that will run an IOError if the file is not in the same folder as the simulator
        try:
            open_file =open(filename) # open file provided
            file_data = open_file.read() # load the whole data to memory
            self.simulation = file_data.split('\n') # splits the data by line into the list(self.simulation)
            open_file.close() # close file provided
            print('Loading Simulation...')
            self.simulation_loaded = True # change self.simulation_loaded

        except IOError as NoFileFound: # run this if the file is not in the file.
            print('There is no file associated with this simulator.')


    ###### This method runs the simulation #######
    def run_simulation(self):

        if self.simulation_loaded is True: # if the Run_simulation worked
            self.direction = 12 # one-time change from 0 to 12 - this simulates a clock.


            for command in self.simulation: # look through list(self.simualtion)

                if command == 'FORWARD': # if the iteration value is 'FORWARD'
                    self.change_gear(FORWARD) # run the method(change_gear) with the global constant FORWARD (1)
                    self.display_stats() # run method(display_stats)

                elif command == 'ACCELERATE': # if the iteration value is 'ACCELERATE'
                    self.accelerate() # run method(accelerate)
                    self.display_stats() # run method(display_stats)

                elif command == 'LEFT': # if the iteration value is 'LEFT'
                    self.turn_steering_wheel(LEFT) # run method(turn_steering_wheel) with global variable LEFT (-1)
                    self.display_stats() # run method(display_stats)

                elif command == 'RIGHT': # if the iteration value is 'RIGHT'
                    self.turn_steering_wheel(RIGHT) # run method(turn_steering_wheel) with global variable RIGHT (1)
                    self.display_stats() # run method(display.stats)

                elif command == 'BRAKE': # if the iteration value is 'BRAKE'
                    self.brake() # run method(brake)
                    self.display_stats() # run method(display_stats)

                elif command == 'REVERSE': # if the iteration value is 'REVERSE'
                    self.change_gear(REVERSE) # run method(change_stats) with global variable REVERSE (0)
                    self.display_stats()

                else: # if the iteration doesn't meet the above criteria.
                    print('This command is not recognised.')
                    pass

        else:
            print('\n')
            print('Please check simulator.txt is in the same folder as this program.')


if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()


