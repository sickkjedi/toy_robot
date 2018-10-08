class Robot(object):
    dirs = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, position):
        self.posX = int(position[0])
        self.posY = int(position[1])
        self.direction = position[2]

    # Move method for changing current robot position, called with MOVE command
    def move(self):
        # Depending on direction, doing a current position check so robot doesn't exit table area
        if self.direction == "NORTH":
            if self.posY < 4: self.posY += 1
        elif self.direction == "EAST":
            if self.posX < 4: self.posX += 1
        elif self.direction == "SOUTH":
            if self.posY > 0: self.posY -= 1
        elif self.direction == "WEST":
            if self.posX > 0: self.posX -= 1

        return self

    # Left method rotates robot direction 90deg to the left
    def left(self):
        # Get index of current direction
        dir_index = self.dirs.index(self.direction)
        # Set new direction 90deg to the left of previous
        self.direction = self.dirs[dir_index - 1]
        return self

    # Right method rotates robot direction 90deg to the right
    def right(self):
        # Get index of current direction
        dir_index = self.dirs.index(self.direction)
        # If "WEST" direction index will go out of range - workaround, not ideal
        if dir_index == 3: dir_index = -1
        # Set new direction 90deg to the right of previous
        self.direction = self.dirs[dir_index + 1]
        return self

    # Print current position and direction on REPORT command call
    def report(self):
        print("Output: " + str(self.posX) + "," + str(self.posY) + "," + self.direction)
        return self


# Function for setting robot location with PLACE command
def place_robot(position):
    # Split PLACE arguments separated by comma into an array
    position = position.split(",")
    # X out of bounds check
    try:
        if int(position[0]) < 0 or int(position[0]) > 4:
            print("Position X out of bounds, use 0-4")
            return None
    except ValueError:
        print("Insert a number for X position")
        return None
    # Y out of bounds check
    try:
        if int(position[1]) < 0 or int(position[1]) > 4:
            print("Position Y out of bounds, use 0-4")
            return None
    except ValueError:
        print("Insert a number for Y position")
        return None
    # Valid direction check
    if position[2] not in Robot.dirs:
        print("Direction not valid, use (NORTH, EAST, SOUTH, WEST)")
        return None

    # Return robot with positions
    return Robot(position)


def main():
    robot = None

    while True:
        # Convert user input to uppercase and split input commands separated by space
        cmd_input = input(">").upper().split()
        # Condition for the first command to be "PLACE", after robot has been instanced it is false
        if cmd_input[0] != "PLACE" and robot is None:
            print("First place the robot using PLACE X,Y,DIR")
            continue

        # Loop going through all user input commands
        for count, command in enumerate(cmd_input):
            if command == "PLACE":
                # Passing the the command immediately after "PLACE" as argument which contains position information
                robot = place_robot(cmd_input[count+1])
                # If place_robot returns None, reiterate while loop
                if robot is None: break
                # Skipping position info as a command
                count += 1

            # LEFT, RIGHT, MOVE and REPORT commands calling their respective methods from robot object
            elif command == "LEFT": robot.left()
            elif command == "RIGHT": robot.right()
            elif command == "MOVE": robot.move()
            elif command == "REPORT": robot.report()
            # EXIT command to end the program
            elif command == "EXIT": return 0


main()
