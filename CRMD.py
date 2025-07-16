# A relationship diagram-drawing program in Python
# using pandas to transfer an Excel table of relationships
# and what the lines are supposed to do
# into Python calculations
# to place the characters at a proper distance around an imaginary circle
# and using Turtle to draw the diagrams
# with each character represented by one symbol to make the diagrams small
# by drawing the symbols and lines between them


# special thanks to Pedro Gaya for pointing out an issue that was slowing the program way down!


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
turtle.speed(0) # This makes Turtle not slow itself down arbitrarily.
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


# This checks if the user wants the program to draw lines all at once for speed or sequentially for beauty.
print("Do you want to 1) watch the program draw the map or 2) have it run as fast as possible? Please type 1 or 2.")
speedrun = input()
print(speedrun) # This checks that the variable is working.
while speedrun != "1" and speedrun != "2":
    print("Ha ha, silly user, you were supposed to type 1 or 2!")
    speedrun = input()
    print(speedrun) # This checks that the variable is working.
speedrun = int(speedrun) # This turns the variable into an integer for the below line.
speedrun -= 1 # This makes it a yes or no question, 0 if not speedrunning and 1 if it is.
print(speedrun) # This checks that the variable is working.


# This imports the relevant Excel sheet into various variables.

# This asks the user for a file path to their relevant data sheet so it can be read from for variables later.
file_path = "" # This sets up the file_path variable, leaving it blank as a condition on which the while loop can be run until it gets a valid file_path.
print("To enter your Excel sheet, please copy its file path, paste it in here, and hit return.") # This prompts the user to drag and drop in a file.
print("If you're not sure how to format the sheet, type anything else below and hit return to get a longer explanation.") # This informs the user of how to trigger the help message.

while file_path == "":
    
    try: # This tries to get a valid file path, leaving if it gets one.
        file_path = input().strip('\'"') # This sets the file path to what the user dragged and dropped in, minus any beginning or ending quotes, which are a common source of errors for this.
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


# This thanks the user for putting in a file path. 
print("Thanks!")


# This advises patience if the user wanted things the non-obvious way, back from when it used to take time to do things the non-obvious way.
#if speedrun == 1:
    #print("Please be patient with this script, as you won't see it do anything until it's done.")


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

# This sets the size of each side of the diagram.
base_side_size = 1800 # This sets a default size of a diagram side in the hypothetical, impossible one-node case.
too_many_nodes = 20 # This sets the point at which diagrams should start dividing their size.
if diagram_nodes_num < too_many_nodes: # This makes diagrams with few nodes have a nice, consistent size that doesn't go off the screen.
    side_size = base_side_size / too_many_nodes
else: # Formerly set to 50, this now makes the side_size get smaller as the diagram gets bigger to make it quicker and less space-consuming to draw diagrams with many nodes.
    side_size = base_side_size / diagram_nodes_num

# This calibrates the size of the angles in the diagram.
# This will be used later to make the cursor move to the correct starting point for the diagram so it'll be properly offset from the center of the diagram.
angle_size = ((diagram_nodes_num - 2) * 180) / diagram_nodes_num

#print(diagram_nodes_num, tilt_per_diagram_side, side_size, angle_size) # This prints the above variables' values to make sure that they're working.


# This calculates the radius of the diagram, printing it at every step to see what, if anything, might go wrong during this process.
#def print_dr(prefix): # This function prints the current state of diagram_radius, prefixed by what was changed since the last time it was printed for better debugging.
#    print(prefix + str(diagram_radius))

# IMPORTANT: Un-comment out the above function if you're going to un-comment out any of the below lines in this code block.
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


# This makes the diagram not draw itself on screen for maximum speed if that's desired by the user.
if speedrun == 1:
    turtle.tracer(0, 0)


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


# A Perplexity function to test if a user-entered color works for coloring a turtle item, and otherwise returns the default color above.
def is_color(color_to_test):
    # Handle NaN (from Excel empty cells) and non-string types up front
    if color_to_test is None or (isinstance(color_to_test, float) and math.isnan(color_to_test)):
        return default_color  # fallback color, e.g., "#000000"
    color_str = str(color_to_test)
    # Now the rest of your logic stays the same, but operates on color_str
    if len(color_str) != 7 or not color_str.startswith("#"):
        return default_color
    try:
        int(color_str.lstrip("#"), 16)
    except Exception:
        return default_color
    return color_str


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



# This entire chunk was pulled from Perplexity to speed up the program, unmodified except where [explicitly noted]. Don't judge my coding skill, reader-senpai!


# Load all relevant columns from Relationships sheet at once
relationships_df = pd.read_excel(file_path, sheet_name='Relationships', usecols="A:C")

# Convert columns to lists
first_nodes  = relationships_df.iloc[:, 0].tolist()  # Column A
second_nodes = relationships_df.iloc[:, 1].tolist()  # Column B
colors       = relationships_df.iloc[:, 2].tolist()  # Column C


# Load both Names and Colors in one go from the Names sheet
names_df = pd.read_excel(file_path, sheet_name='Names', usecols="A,B")
names_list = names_df.iloc[:, 0].tolist()     # Column A: Short names
name_colors = names_df.iloc[:, 1].tolist()    # Column B: Name colors


# ]This makes the turtle go to a node entered given the correct column of data to pull from the Excel table, needed for moving to the node on each end of a relationship.]
def go_to_node(next_character):
    global should_i_draw  # [This summons in the global variable that checks if all this is working.]

    did_it_work = False  # [This is a variable that will be changed to True if the function can find a name.]
    name_iterator = 0

    while name_iterator < len(names_list):  # [so while it's still looking for the desired character to draw a line from or to]
        if names_list[name_iterator] == next_character:
            turtle.goto(node_coordinates[name_iterator])  # [start or end the line here, this is the right character]
            did_it_work = True
            break  # [okay we got the right character, time for a lunch break]
        name_iterator += 1  # [no that wasn't the right character, keep going]

    should_i_draw = did_it_work  # Set draw flag based on result

    # [Formerly thought that, if the character couldn't be found, the user needs to be aware of it. Then that annoyed me, so now it's commented out.]
    #if not did_it_work:
    #    print(f"Character '{next_character}' not found.")


for i in range(len(first_nodes)):  # same as relationships_num
    go_to_node(first_nodes[i])  # [This makes the turtle jump to the f]irst character in the relationship

    # [This makes the cursor start drawing a relationship if it's found appropriate nodes to draw the relationship between.\
    if should_i_draw:
        turtle.pendown()

    # Set color from preloaded list
    turtle.pencolor(is_color(colors[i]))

    go_to_node(second_nodes[i])  # [This makes the turtle jump to the s]econd character in the relationship

    turtle.penup() # [This makes the cursor finish drawing a relationship.]


# [This draws all the node names.]
# [It draws them after the relationship lines between them have been drawn]
# [so they'll appear over the lines instead of under them]
# [and thus are legible even in diagrams with many lines.]

turtle.goto(node_coordinates[0])  # Prepare to print node names at the correct location

for i in range(diagram_nodes_num):
    next_name = names_list[i]
    next_color = name_colors[i]

    # Set the turtle color to the color from your Excel sheet, or a default if invalid
    safe_color = is_color(name_colors[i])
    turtle.color(safe_color)

    turtle.write(next_name)  # Write the node name at the current location

    # Move to the location of the next node in the diagram
    turtle.penup()  # [This prevents Turtle from drawing a line following the cursor.]
    turtle.setheading((i+1)*tilt_per_diagram_side)  # [This sets the cursor to the right angle given the number of diagram sides and the number of nodes already drawn so it can easily draw the next node.]
    turtle.forward(side_size)


# Perplexity input ends here.



turtle.hideturtle() # This removes the cursor so it doesn't get in the way of screenshots.

# This makes the program show changes if they've been disabled during drawing for speed by the user.
if speedrun == 1:
    turtle.update()
    
print("Now, all that's left is to take a screenshot of your diagram!")
print("Once you're done, close the diagram's window to end the program.")
turtle.done() # This helps users screenshot the diagram by keeping Turtle from eating it.
