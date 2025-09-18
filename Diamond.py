"""
This was created with my partner Mr.Andres
September 8th, 2025
"""

#required number variables
#String variables required
#This is going to do my top part
#I'm using a method/function to organize
counter = 0
rowsDrawn = 0
spacesOutside = 0
spacesInside = 0
starsToDraw = 0
userInput = 0
output = ""

# Ask user for input (must be odd between 1 and 13)
while True:
    userInput = int(input("Enter an odd number from 1 to 13: "))
    if userInput % 2 == 1 and 1 <= userInput <= 13:
        break

# Top half of diamond
spacesOutside = userInput // 2
spacesInside = -1  # No inside spaces on first row
rowsDrawn = 0

while rowsDrawn < (userInput // 2 + 1):
    output = ""

    # Draw spaces before first star
    for counter in range(spacesOutside):
        output += " "

    # Draw first star
    output += "*"

    # Draw inside spaces (only if not the very top row)
    if spacesInside >= 1:
        for counter in range(spacesInside):
            output += " "
        # Draw second star
        output += "*"

    print(output)

    # Prepare for next iteration
    rowsDrawn += 1
    spacesOutside -= 1
    spacesInside += 2

# Bottom half of diamond
spacesOutside = 1
spacesInside = userInput - 4  # adjust for hollow spacing
rowsDrawn = 0

while rowsDrawn < (userInput // 2):
    output = ""

    # Draw spaces before first star
    for counter in range(spacesOutside):
        output += " "

    # Draw first star
    output += "*"

    # Draw inside spaces
    if spacesInside >= 1:
        for counter in range(spacesInside):
            output += " "
        output += "*"

    print(output)

    # Prepare for next iteration
    rowsDrawn += 1
    spacesOutside += 1
    spacesInside -= 2