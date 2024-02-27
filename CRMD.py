# A relationship diagram-drawing program in Python
# using pandas to transfer an Excel table of relationships
# and what the lines are supposed to do
# into Python calculations
# to place the characters at a proper distance around an imaginary circle
# and using Turtle to draw the diagrams
# with each character represented by one symbol to make the diagrams small
# by drawing the symbols and lines between them


# This attempts to pacify users while the program boots up, which may take a while if you're running it for the first time in a given session of an environment.
print("Welcome to the Character Relationship Map Drawer!")

# This prints the number input as the percent of the way done loading the program is.
# This function will be used repeatedly during the module loading sequence,
# which is the part of the program that can take a while when the environment is first run.
def loading(percent):
    if percent != 100: # This prints a standard message for when loading is in progress.
        print("%s percent..." % (percent))
    else: # This prints a special message for when loading is complete.
        print("%s percent!" % (percent))

#loading(0) # This simultaneously tests the function above and tells users how far they are through the loading process.


# This imports all the modules and prints test lines and loading status indicators to pacify users, as this can take a while.
import turtle # This will let me draw the diagrams properly.
#loading(20)
import math # This will let me offset the diagram from the center properly.
#loading(40)
import random # This will let me get random numbers to test the program properly.
#loading(60)
print("This will take an Excel sheet of characters and relationships and draw a character relationship map from this data!") # This prints an info message while loading, as the following module takes a while to import.
import pandas as pd # This will let me connect the program to Pandas to use user-input tables, with Pandas imported as "pd" because that's what all the documentation expects.
#loading(80)
import numbers # This lets me test if user-input color strings are correct.
#loading(100)

# test lines
#print("Hello world!") # test line
#print(turtle.xcor(), turtle.ycor()) # This shows where the cursor starts at for reference.


# This imports the relevant Excel sheet into various variables.

# This asks the user for a file path to their relevant data sheet so it can be read from for variables later.
file_path = "" # This sets up the file_path variable, leaving it blank as a condition on which the while loop can be run until it gets a valid file_path.
print("To enter your Excel sheet, please copy its file path, then paste it in here, and finally hit return.") # This prompts the user to drag and drop in a file.
print("If you're not sure how to format the sheet, type anything else below and hit return to get a longer explanation.") # This informs the user of how to trigger the help message.

while file_path == "":
    
    try: # This tries to get a valid file path, leaving if it gets one.
        file_path = input() # This sets the file path to what the user dragged and dropped in.
        #print(file_path) # This is a test line that displays the file path dropped in to make sure it's right.

        # This imports the list of names from the data sheet into a variable called "names" for quick access later.
        names = pd.read_excel(file_path, sheet_name='Names', index_col=0, header=0, usecols="A") # This just reads the first column of the Names sheet of the fed-in Excel file, thus saving what names are to be displayed in the diagram to this variable so they can be displayed later.
        #print(names) # This prints what I've just gotten for testing purposes.

        division_by_zero = len(names) / len(names) # This tests to see if there's actually anything in names, as if there isn't, the program will crash when it leaves the loop.
        #print(division_by_zero) # This prints what I've just gotten for testing purposes.

        break # This continues the program if it gets a valid file_path.
    
    except: # If there isn't a valid file path, this blanks the file_path variable to cause the loop to run again, as well as explaining the program to the user.
        file_path = ""
        print("To make the program work, please add the Excel sheet of your character relationship map.")
        print("Excel sheets should have two sheets:")
        print("one called Names (in title case), with what will render for your characters' names in the first column and any hex colors to color those names in the second;")
        print("and one called Relationships (in title case), with each pair of characters who have a relationship enumerated along with their hex colors.")
        print("For example, if you have characters X and Y defined in Names, you might have a Relationships row where X is in the first column, Y in the second, and #000000 in the third to make a black line between X and Y.")
        print("To enter your Excel sheet, please copy its file path, then paste it in here, and finally hit return.") # This prompts the user to drag and drop in a file.


# This imports the list of colors from the data sheet into a variable called "name_colors" for quick access later, something I thought I'd use in an earlier version of the program but now realize I don't.
#name_colors = pd.read_excel(file_path, sheet_name='Names', index_col=0, header=0, usecols="B") # This just reads the second column of the Names sheet of the fed-in Excel file, thus saving what colors are to be displayed in the diagram to this variable so they can be displayed later.
#print(name_colors) # This prints what I've just gotten for testing purposes.


# This sets the number of nodes in the diagram and subsequent variables.
# This number will be used to specify size and number of sides for the polygon that the diagram is shaped like,
# with each node causing an additional side of the polygon and making the diagram bigger.

diagram_nodes_num = len(names) # This sets the number of nodes itself to the number of names there are in the Excel sheet fed into this program, that being the number of characters in the diagram and consequently the number of nodes there should be in the sheet.
#print(diagram_nodes_num) # This is a test case to make sure that I have the diagram_nodes_num working right.

#diagram_nodes_num = random.randint(3, 32) # As a test in lieu of an Excel sheet, this sets the number of nodes itself, currently to a random number between 3 and 32 (32 being the largest I can conceive of needing).

tilt_per_diagram_side = 360 / diagram_nodes_num # This sets the amount that the cursor should tilt per side of the diagram to make it the right shape.
side_size = 50 # This sets the size of each side of the diagram.

# This calibrates the size of the angles in the diagram.
# This will be used later to make the cursor move to the correct starting point for the diagram so it'll be properly offset from the center of the diagram.
angle_size = ((diagram_nodes_num - 2) * 180) / diagram_nodes_num

#print(diagram_nodes_num, tilt_per_diagram_side, side_size, angle_size) # This prints the above variables' values to make sure that they're working.


# This calculates the radius of the diagram, printing it at every step to see what, if anything, went wrong.
#def print_dr(prefix): # This function prints the current state of diagram_radius, prefixed by what was changed since the last time it was printed for better debugging.
#    print(prefix + str(diagram_radius))

#print("Now it's time to make a new variable that gives the radius of the diagram we'll draw, which mathematically is supposed to be the number of sides of the polygon divided by (2 times the sine of (180 divided by the number of nodes in the diagram))")
diagram_radius = 180/diagram_nodes_num
#print_dr("Dividing the number of nodes by 180 yields ")
diagram_radius = math.radians(diagram_radius)
#print_dr("Turning this number from degrees into radians so I can do the sine of this in the math module (which only takes radians) yields ")
diagram_radius = math.sin(diagram_radius)
#print_dr("Taking the sine of this then yields ")
diagram_radius = 2*diagram_radius
#print_dr("Multiplying this by 2 then yields ")
diagram_radius = side_size/diagram_radius
#print_dr("And then, finally, dividing this all by the number of sides in the diagram yields ")

# These test cases assign diagram_radius to the old, faulty formula that I wasn't able to test without breaking it up into bits as above.
# Turns out the problem is that 180/diagram_nodes_num isn't surrounded by math.radians().
#diagram_radius = side_size/(2*math.sin(180/diagram_nodes_num))
#print_dr("Also, when we did this by the old formula, we got")


# This moves the cursor far enough from the center that the diagram is centered on the center of the screen.

#turtle.dot(1, "green") # This marks the center of the screen for reference. If this reference is needed, un-comment this line.
turtle.penup() # This keeps turtle from making lines as it moves away from the center of the screen to the starting point of the diagram.

# This moves the cursor away from the center in the opposite direction from where the farthest node from the starting point will be to place the diagram as a whole centered on the center of the screen.
turtle.setheading(360 - (angle_size / 2)) # This angles the cursor in the right direction for the diagram to be offset to draw an invisible radius.
turtle.forward(diagram_radius) # This draws an invisible radius.
turtle.setheading(0) # This angles the cursor in the right direction to draw the rest of the nodes.


# This generates a totally random hex color,
# e.g. a 6-digit hex number between 0 and 2^24-1, or 16777215
# (as each digit in hex is a number between 0 and 2^4-1, or 15, and I need 6 digits),
# for usage anywhere in the program where I may need a test color.

# This makes the function explained above.
def random_color():
    new_color = random.randint(0, 16777215) # This generates a new number that can be turned into a hex color.
    #print(str(new_color)) # This prints the color as a test line to make sure that the function is working.

    # This generates a new hex color as a 6-digit hexadecimal number.
    # The following line is courtesy of https://www.geeksforgeeks.org/python-hex-function/
    # hex(number).lstrip("0x").rstrip("L")
    # Thanks guys!
    new_color = hex(new_color).lstrip("0x").rstrip("L")
    
    #print(str(new_color)) # This prints the example color again to make sure that it's working as a hexadecimal number.

    # This prints an error message in case the color is #000000 and so doesn't render in the above message.
    #if str(new_color)=="":
    #    print("Yo, the previous line seems to have not rendered because the color obtained was black, or #000000. Not sure why that happens, but don't worry about it, OK?")

    # This makes the color always be 6 digits long, even if it would be shorter otherwise, so that Turtle won't reject it as a hex color.
    # This line was borrowed from Stanislav Koncebovski
    # ( https://stackoverflow.com/users/15198069/stanislav-koncebovski )
    # in a response to this post:
    # https://stackoverflow.com/a/339024
    # Thanks Stanislav!
    new_color = new_color.rjust(6, '0')

    #print(str(new_color)) # This prints the example color one last time as a test line to make sure that the digit adjustment is working.
    return '#%s' % (new_color) # This packages up the hexadecimal number in a format where Turtle will be able to use it.


default_color = "#000000" # This sets black as a default color for usage in the following function.


# This tests if a user-entered color works for coloring a turtle item, and otherwise returns black as a default color.
# It checks to see if the color_to_test is formatted properly, as #XXXXXX, where each X is a hexadecimal number. If not, it returns the color black and prints an error message.
def is_color(color_to_test):
    #def color_error_message(): # The following is a test line that tells the developer that broken colors are broken.
        #print("A correct color for this name was not specified. Correct colors should be 7 characters long, with the first character being a # sign and the other 6 characters being numbers.")

    # This checks to see if the second argument below, which checks if a hex color input begins with # (and so is a hex color), works at all.
    # This is because the program crashed and said that the second argument was invaild in a previous version where only the second argument was specified.
    # Specifically, the error message was:
    # AttributeError: 'DataFrame' object has no attribute 'startswith'
    #try: # This sees if the second argument below works at all by having it print based on whether or not the value in question begins with a # or not.
    #    if color_to_test.startswith("#"):
    #        print("#!")
    #    else:
    #        print("No # :(")
    #except: # If the second argument below doesn't work, now we know that's a glitch and needs to be addressed, and maybe is the source of other glitches as well.
    #    print("Hash checking isn't working. Hash spotting will be needed.")

    # The first if argument checks if the color_to_test is 7 characters.
    # THe second checks if it begins with #.
    if len(color_to_test) != 7 or color_to_test.startswith("#") == False:
        color_to_test = default_color
        #color_error_message() This runs a test error message line. Before un-commenting this, un-comment the def color_error_message() line and the line succeeding it.

    # The third checks if the other 6 characters, when converted from hexadecimal into decimal, are numbers.
    try:
        isinstance(int(color_to_test.lstrip("#"), 16), numbers.Number)
    except:
        color_to_test = default_color
        #color_error_message() This runs a test error message line. Before un-commenting this, un-comment the def color_error_message() line and the line succeeding it.

    return color_to_test # This returns either the original color or an error color.

# These test if the above function is working.
#print(is_color("#007FFF")) # This tests to ensure that nothing is blocking working values.
#print(is_color("#7FFF")) # This tests if the length (first) parameter is working.
#print(is_color("007FFF")) # This tests if the # (second) parameter is working.
#print(is_color("#TISTYY")) # This tests if the number (third) parameter is working.
#print(is_color("7FFF")) # This tests if the first and second (length and #) parameters are working.
#print(is_color("#TISTY")) # This tests if the first and third parameters (length and numbers) are working.
#print(is_color("TISTYYY")) # This tests if the second and third parameters (# and numbers) are working.
#print(is_color("TISTY")) # This tests if all parameters in the above function working.


# This figures out where all the nodes will be in the diagram, then draws them (counter-clockwise), adding each one to a list as it does so so relationship lines can be drawn between the nodes later.

# This uses the Excel list of nodes to figure out the number of nodes 

node_coordinates = [] # This makes a list that node coordinate tuples will be added to when the nodes are drawn so that relationship lines can be drawn between the nodes later.
#print(node_coordinates) # This is a test line that prints the current state of the node_coordinates list so we can make sure it's working.

for i in range(diagram_nodes_num): # This draws the vertices in a polygonal diagram.

    # This logs the current node_coordinates.
    # This code was formerly at the end of the loop, but that meant that it indexed the first node at the end of the list, second node first, and so on, which would draw relationships incorrectly.
    current_coordinates = (turtle.xcor(), turtle.ycor()) # This turns where the cursor ends at (the location of the node in question) into a tuple so it can be added to the below.
    node_coordinates.append(current_coordinates) # This adds the above to the list of node coordinates so that relationship lines can be drawn between the nodes later.
    #print(node_coordinates) # This is a test line that prints the current state of the node_coordinates list so we can make sure it's working.

    turtle.setheading((i+1)*tilt_per_diagram_side) # This sets the cursor to the right angle given the number of diagram sides and the number of nodes already drawn so it can easily draw the next node.
    turtle.forward(side_size) # This is an attempt to see my black dot without the cursor sitting on it.


# This initializes all the variables for drawing all the relationships in the diagram.

# This creates the number of all relationships.
# The first line just takes the length of a representative column of the Relationships sheet of the fed-in Excel file to get the number of relationships in the diagram.
# Note that this includes lines that don't have any values in the leftmost column as long as they're lines in the Excel table followed by other lines with values in the table.
relationships_num = len(pd.read_excel(file_path, sheet_name='Relationships', index_col=0, header=0, usecols="A"))
#relationships_num = random.randint(1, diagram_nodes_num) # This sets the number of relationships to a random number that isn't more than there are nodes to avoid it making too many repeat lines in triangular diagrams.
#print(relationships_num) # This makes sure that the relationships_num variable is working.

# This creates the number of all character names.
# The first line just takes the length of a representative column of the Relationships sheet of the fed-in Excel file to get the number of relationships in the diagram.
# Note that this includes lines that don't have any values in the leftmost column as long as they're lines in the Excel table followed by other lines with values in the table.
names_num = len(pd.read_excel(file_path, sheet_name='Names', index_col=0, header=0, usecols="A"))
#print(names_num) # This makes sure that the names_num variable is working.

# This returns the coordinates of a random node in the table, for usage in testing in the relationship-line-drawing loop.
def random_node_coordinates():
    return node_coordinates[random.randint(0,len(node_coordinates)-1)]

should_i_draw = True # This is a variable that will be changed to True in the following function if the Excel syntax is entered properly.


# This makes the turtle go to a node entered given the correct column of data to pull from the Excel table, needed for moving to the node on each end of a relationship.
def go_to_node(column):

    #print("Hello, world!") # This tests to make sure that the loop is working.

    # This attempts to see if a given Relationship value is bigger than 0; if it doesn't, the program says it doesn't have the right value; if it breaks, it delivers the Python error message and keeps going.
    try:
        # This pulls the value for the first character in the relationship.
        next_character_raw = pd.read_excel(file_path, sheet_name='Relationships', index_col=None, header=0, usecols=column, skiprows=i+1, nrows=0) # This pulls the first character's name.
        next_character = next_character_raw.columns.values[0] # This turns the next_color_raw into a color value that can easily be used by the Python code.
        #print(next_character) # This is a test line to ensure that the next_character pulling is working.

        did_it_work = False # This is a variable that will be changed to True if the function can find a name.
        #print(did_it_work) # This checks to see if the above is working.
        
        # This looks through the Characters sheet to try to match next_character to a character in that sheet to move the cursor to.
        name_iterator = 0 # This sets a variable to 0 so it can iterate through the list of characters to try to match the value entered to a character value.
        while name_iterator < names_num: # This iterates through name_iterator, trying to find a name that matches; if it does, it will move there; otherwise, it'll go on regardless.
            current_name_raw = pd.read_excel(file_path, sheet_name='Names', index_col=None, header=0, usecols="A", skiprows=name_iterator+1, nrows=0) # This pulls a character name to try to match next_character to. 
            current_name = current_name_raw.columns.values[0] # This turns the current_name_raw into a color value that can easily be used by the Python code.
            #print(current_name) # This makes sure that current_name is working. Don't un-comment unless this is really needed, otherwise you'll get a very long list of data.

            if current_name == next_character:
                turtle.goto(node_coordinates[name_iterator])
                #print("Yo, it worked!") # This makes sure that the loop is working.
                did_it_work = True # This sets the variable established earlier for the sole purpose of being set to True if this finds a first node to True if this finds a first node.

            name_iterator += 1 # This restarts the loop.

        # This makes the cursor not draw a node from where it last was to a second node if it can find a second node but not a first node.
        global should_i_draw # This summons in the global variable that checks if all this is working.
        should_i_draw = True # This sets it to True just in case it was False last. It should be True unless it can't find the right node.
        if did_it_work == False: # This sets the above variable to False if it can't find the second node.
            should_i_draw = False
            
        # This checks to see if the above is working.
        #print(did_it_work)
        #print(should_i_draw)
        
    except:
        print("IndexError: index 0 is out of bounds for axis 0 with size 0")

        
# This draws all the relationship lines between the nodes in the diagram.
for i in range(relationships_num): # This line iterates through the number of all the relationships in the Excel table.
    go_to_node("A") # This makes the turtle jump to the point needed for the first node in a relationship.
    #turtle.goto(random_node_coordinates()) # This makes the turtle jump to a random point in the table to begin drawing a test relationship.

    if should_i_draw == True: # This makes the cursor start drawing a relationship if it's found appropriate nodes to draw the relationship between.
        turtle.pendown() # This makes the cursor start drawing a relationship.

    # This sets the pencolor to the color specified in Excel if it finds one, and otherwise sets the pencolor to default.
    turtle.pencolor(is_color(pd.read_excel(file_path, sheet_name='Relationships', index_col=None, header=0, usecols="C", skiprows=i+1, nrows=0).columns.values[0]))    
    #turtle.pencolor(random_color()) # This makes the relationship that the cursor will draw be a randomly colored line.

    go_to_node("B") # This makes the turtle jump to the point needed for the second node in a relationship.
    #turtle.goto(random_node_coordinates()) # This makes the cursor draw a random relationship.
    turtle.penup() # This makes the cursor finish drawing a relationship.


# This draws all the node names.
# It draws them after the relationship lines between them have been drawn
# so they'll appear over the lines instead of under them
# and thus are legible even in diagrams with many lines.

turtle.goto(node_coordinates[0]) # This moves the turtle to the location of the first node before printing the names.

for i in range(diagram_nodes_num): # This calls on the number of vertices again to draw that many node names.
    
    # This reads the relevant shorthand name from the relevant column and next row up for drawing in the diagram of the Names sheet of the fed-in Excel file,
    # thus saving what names are to be displayed in the diagram to this variable so they can be displayed later.
    # "skiprows=i+1" skips a number of rows equal to the iterator, printing the correct value on each line.
    # Don't change it from being equal to "i" to being equal to a static value (like "1"), or the program will only print one value every time.
    # "skiprows=i" prints the header value as the first value and doesn't print the last value, hence "i+1".
    next_name = pd.read_excel(file_path, sheet_name='Names', index_col=None, header=0, usecols="A", skiprows=i+1, nrows=0) # This pulls the shorthand name.

    # This reads the relevant shorthand name from the relevant column and next row up for drawing in the diagram of the Names sheet of the fed-in Excel file,
    # thus saving what names are to be displayed in the diagram to this variable so they can be displayed later.
    # "skiprows=i+1" skips a number of rows equal to the iterator, printing the correct value on each line.
    # Don't change it from being equal to "i" to being equal to a static value (like "1"), or the program will only print one value every time.
    # "skiprows=i" prints the header value as the first value and doesn't print the last value, hence "i+1".
    next_color_raw = pd.read_excel(file_path, sheet_name='Names', index_col=None, header=0, usecols="B", skiprows=i+1, nrows=0) # This pulls the name color.
    next_color = next_color_raw.columns.values[0] # This turns the next_color_raw into a color value that can easily be used by the Python code.
    #print(next_color) # This is a test line to ensure that the next_color pulling is working.

    # This prints the character names pulled above in the colors pulled above (or black, if a broken color cell has been pulled, printing that the color is broken if not absent).
    turtle.color("blue") # This is a test line to ensure that the below line is working properly.
    turtle.color(is_color(next_color)) # This sets the color of the node to the color input in the Excel sheet, or black if the color entered isn't correct.
    turtle.write(next_name.columns.values[0]) # This writes the shorthand name pulled above.
    #turtle.dot(2, random_color()) # This is a test line that draws a randomly colored dot on the screen.

    # This moves to the location of the next node in the diagram.
    turtle.penup() # This prevents Turtle from drawing a line following the cursor.
    turtle.setheading((i+1)*tilt_per_diagram_side) # This sets the cursor to the right angle given the number of diagram sides and the number of nodes already drawn so it can easily draw the next node.
    turtle.forward(side_size) # This is an attempt to see my black dot without the cursor sitting on it.


# This sends the cursor way off in the bottom-right corner where it shouldn't get into screenshots.
print("Now, all that's left is to take a screenshot of your diagram!") # This prompts the user to take a screenshot of the diagram before the program ends.
final_x = diagram_nodes_num * 100 # This creates the x coordinate for the bottom-right corner. "*1000" puts it significantly far from the center, even on small diagrams.
final_y = diagram_nodes_num * -100 # This creates the y coordinate for the bottom-right corner. "*-1000" puts it significantly far from the center, even on small diagrams.
#print(final_x, " ", final_y) # This prints the x and y coordinates to make sure they're good.
turtle.goto(final_x, final_y) # This sends the turtle into the bottom-right corner.


# This prompts the again to take a screenshot of the diagram before the program ends.
print("Once you're done, hit return to end the program. Warning: This may get rid of your diagram, so make sure to take a screenshot first!")
program_ending = input() # This makes a new variable that will never be used again just to get the program to end only when the user hits return.
