# Marcin Grelewicz (s17692) NAI 
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_tx = initial_tx
current_ty = initial_ty

# game loop
while 1:
    remaining_turns = int(input())
    move_x = ""
    move_y = ""
    
    if light_x < current_tx:
        current_tx -= 1
        move_x = "W"
    elif light_x > current_tx:
        current_tx += 1
        move_y = "E"
   
   if light_y < current_ty:
        current_ty -= 1
        move_y = "N"
    elif light_y > current_ty:
        current_ty += 1
        move_y = "S"
    
    print(move_y + move_x)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    #print("SE")
