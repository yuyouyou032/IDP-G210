from colorSensors import colorDetector
# from mechanism import pickBox, liftUp, liftDown
from distanceSensors import getDistFromUltrasonic, Distance
from motors import wheels_forward, wheels_backward, stop
from utime import sleep

dist = Distance()
def hasBox():
    sleep(0.5)
    distance = dist.getDistFromTMF8x01()
    if distance >200 or distance == 0:
        print(f"Distance = {distance} mm, No box detected")
        return False
    print(f"Distance = {distance} mm, Box detected")
    return True

def scanBottomLevel(rackId):
    """
    Scan the bottom level of a rack.

    Steps:
    1. Enter the rack at ground level.
    2. Check if a box exists on the bottom shelf.
    3. If a box is found:
         - Detect its color
         - Pick it up
         - Back out to the rack entrance with the box
       Return (True, color)
    4. If no box is found:
         - Back out to the rack entrance without a box
       Return (False, None)
    """
    # From: rack entrance, facing rack
    # To: rack entrance, facing rack
    # currentRackPos unchanged

    # Move robot into the bottom-level scanning position
    wheels_forward(t=1)  # To bottom scan point
    if hasBox():
        # alignToBottomBox()  
        # pickBox()
        color = colorDetector()                   
        # Move back to the rack entrance while holding the box
        wheels_backward(t=1)
        print("True, color")
        return True, color
    else:
        # No box detected — back out to the entrance
        wheels_backward(t=1)
        return False, None

def scanTopLevel(rackId):
    """
    Scan the top level of a rack.

    Steps:
    1. Enter rack at ground level.
    2. Lift the mechanism to the upper level.
    3. If a box exists on the upper level:
         - Align to the box
         - Detect its color
         - Pick the box
         - Lower the lift
         - Exit back to rack entrance with the box
         - Return (True, color)
    4. If no box:
         - Lower the lift
         - Exit back to rack entrance without box
         - Return (False, None)
    """

    # Move robot into rack at ground level
    wheels_forward(t=1)  # To bottom scan point
    liftUp()
    if hasBox():
        # alignToUpperBox()
        color = colorDetector()
        pickBox()
        liftDown()
        # Return to entrance with box
        wheels_backward(t=1)
        return True, color
    else:
        # No box found
        liftDown()
        wheels_backward(t=1)
        return False, None

