from utime import sleep
from lineSensors import lineFollowStep, sensor1234
from motors import wheels_forward, wheels_backward, stop, left_pivot, right_pivot, half_turn_L, half_turn_R
from distanceSensors import getDistFromUltrasonic
import state
from mechanism import dropBox

def useUltrasonic():
    while True:
        lineFollowStep()
        d = getDistFromUltrasonic()
        print("Distance:", d, "cm")
        if d < 20:
            stop()
            break
    print("complete")

def moveBackToStartBox():
    left_pivot()
    wheels_forward(t=0.5)
    while True:
        lineFollowStep()
        d = getDistFromUltrasonic()
        print("Distance:", d, "cm")
        if d < 90:
            stop()
            break
        sleep(0.03)
    right_pivot(t=2.7)
    wheels_forward(t=0.5)
    while True:
                lineFollowStep()
                d = getDistFromUltrasonic()
                print("Distance:", d, "cm")
                if d < 20:
                    stop()
                    break
    
def navigateStartBoxToLeftRowFirstRackEntry(): 
    # From: start box
    # To: left row, first rack entry (A6), facing rack
    # currentRackPos = 6
    print("Navigating from Start Box to First Rack Entry")
    wheels_forward()
    print("Stage 1: Moving forward until first 1111...")
    while True:
        lineFollowStep()
        readings = sensor1234()   # e.g. [1,1,1,1]
        print("Line sensors:", readings)
        if readings == [1,1,1,1]:
            print("Detected 1111")
            stop()
            break
        sleep(0.05)
    sleep(0.2)

    # Turn LEFT 
    print("Turning left")
    left_pivot()

    # Drive forward until distance < 5cm
    print("Driving forward to hub...")
    while True:
        lineFollowStep()
        d = getDistFromUltrasonic()
        print("Distance:", d, "cm")
        if d < 16:
            stop()
            break
    right_pivot(t=2.7)
    while True:
        lineFollowStep()
        readings = sensor1234()   # e.g. [1,1,1,1]
        print("Line sensors:", readings)
        if readings == [1,1,1,0]:
            print("Detected 1110 - Rack entry")
            stop()
            break
    right_pivot(t=2.6)
    print("Arrived at rack entry!")

def navigateFromLeftRowToRightRowFirstRackEntry():
    right_pivot()
    wheels_forward(t=0.5)
    while True:
        lineFollowStep()
        readings = sensor1234()   
        if readings == [1,1,0,1]:
            print("Hub(left) detected.")
            stop()
            break
        sleep(0.05)
    left_pivot()  
    wheels_forward(t=0.5)
    while True:
        lineFollowStep()
        readings = sensor1234()   
        if readings == [1,1,1,1]:
            print("Hub(right) detected.")
            stop()
            break
        sleep(0.05)
    left_pivot()
    wheels_forward(t=0.5)
    while True:
        lineFollowStep()
        readings = sensor1234()   
        if readings == [1,1,0,1]:
            print("Rack entry detected.")
            stop()
            break
        sleep(0.05)
    left_pivot()
    

def goToRackEntrance(targetRack, side):
    if state.currentRackPos == targetRack:
        return 
    if side == 'Left':
        # Otherwise move to the rack entrance
        wheels_forward(t=0.5)           # Move clear of the previous rack
        while True:
            lineFollowStep()
            readings = sensor1234()   
            if readings == [1,1,1,0]:
                print("Rack entrance detected.")
                stop()
                break
            sleep(0.05)
        right_pivot()                 # Face the rack again
        
    # Update state
    else:
        pass
    state.currentRackPos = targetRack

def deliverFromRack(rackID, color, side):
    # From: at rack entrance (rackID), facing rack, carrying box
    # To: at rack entrance (rackID), facing rack, hands empty
    goAlongRowMainToHub(rackID, side)
    goFromHubToColorBay(color, side)
    dropBox()
    goFromColorBayBackToHub(color, side)
    goFromHubBackToRowMain(rackID, side) 
    state.currentRackPos = rackID


def moveToPreviousRackEntry(rackID, side):
    # From: at rack entrance (rackID), facing rack
    # To: at rack entrance (rackID-1), facing rack
    if side == 'Left':
        while True:
            wheels_backward(t=0.5)
            readings = sensor1234()   
            if readings == [1,1,1,1]:
                print("Time to turn left.")
                stop()
                break
            sleep(0.05)
        left_pivot(t=2.7)                  # Turn into aisle
        while True:
            wheels_backward(t=0.2)
            readings = sensor1234()   
            if readings == [1,1,1,0]:
                print("Previous rack entrance detected.")
                wheels_backward(t=0.1)
                stop()
                break
            sleep(0.05)
        right_pivot(t=2.7)                 # Face the rack again
    else:
        pass
    state.currentRackPos = rackID - 1

def navigateFromCurrentRackEntryToStartBox(side):
    if side == 'Left':
        while True:
            wheels_backward(t=0.5)
            readings = sensor1234()   
            if readings == [1,1,1,1]:
                print("Time to turn right.")
                stop()
                break
            sleep(0.05)
        right_pivot(t=2.7)
        wheels_forward(t=0.5)
        while True:
            lineFollowStep()
            d = getDistFromUltrasonic()
            print("Distance:", d, "cm")
            if d < 61:
                stop()
                break
            sleep(0.5)
        left_pivot()
        wheels_forward(t=0.5)
        count_1110 = 0
        junction_lock = False
        while True:
            lineFollowStep()
            s = sensor1234()
            if s == [1,1,1,0] and not junction_lock:
                count_1110 += 1
                junction_lock = True    # lock further detections
                print("Detected 1110 #", count_1110)
            # Unlock only after junction pattern goes away
            if s != [1,1,1,0]:
                junction_lock = False
            if count_1110 == 2:
                stop()
                break
            sleep(0.1)
        right_pivot(2.7)
        wheels_forward(t=0.5)
    else:
        pass

def goAlongRowMainToHub(rackID, side):
    # To : at hub, facing color bays
    if side == 'Left':
        while True:
            wheels_backward(t=0.5)
            readings = sensor1234()   
            if readings == [1,1,1,1]:
                print("Time to turn right.")
                stop()
                break
            sleep(0.05)
        right_pivot(t=2.7)
        wheels_forward(t=0.5)
        while True:
            lineFollowStep()
            d = getDistFromUltrasonic()
            print("Distance:", d, "cm")
            if d < 61:
                stop()
                return
#             s = sensor1234()
#             if s == [1,1,0,1]:
#                 count_1101 += 1
#                 print("Detected 1101 #", count_1101)
#                 if count_1101 == 7-rackID:
#                     stop()
#                     return
            sleep(0.03)
    else:
        pass    
    
def goFromHubToColorBay(color, side):
    if side == 'Left':
        if color == 'GREEN':
            left_pivot()
            wheels_forward(t=0.5)
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,0]:
                    stop()
                    break
                sleep(0.03)
            right_pivot(t=2.7)
            wheels_forward(t=0.5)
        elif color == 'YELLOW':
            left_pivot(t=2.5)
            wheels_forward(t=0.5)
            count_1110 = 0
            junction_lock = False
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,0] and not junction_lock:
                    count_1110 += 1
                    junction_lock = True    # lock further detections
                    print("Detected 1110 #", count_1110)
                # Unlock only after junction pattern goes away
                if s != [1,1,1,0]:
                    junction_lock = False
                if count_1110 == 3:
                    stop()
                    break
                sleep(0.1)
            right_pivot(t=2.7)
            wheels_forward(t=0.5)
        elif color == 'RED':
            left_pivot()
            wheels_forward(t=0.5)
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,1]:
                    stop()
                    break
                sleep(0.03)
            right_pivot(t=2.7)
            wheels_forward(t=0.5)
        while True:
            lineFollowStep()
            d = getDistFromUltrasonic()
            print("Distance:", d, "cm")
            if d < 20:
                stop()
                break
    else:
        pass

def goFromColorBayBackToHub(color, side):
    if side == 'Left':
        if color == "BLUE":
            half_turn_L()
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,0]:
                    stop()
                    break
                sleep(0.03)
        else:
            half_turn_R()
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,1] or s == [1,1,0,1]:
                    stop()
                    break
                sleep(0.03)
            left_pivot()
            wheels_forward(t=0.5)
            while True:
                lineFollowStep()
                s = sensor1234()
                if s == [1,1,1,1]:
                    stop()
                    break
                sleep(0.03)
            right_pivot(t=2.7)
    else:
        pass

def goFromHubBackToRowMain(rackID, side):
    if side == 'Left':
        count_1110 = 0
        junction_lock = False
        while True:
            lineFollowStep()
            s = sensor1234()
            if s == [1,1,1,0] and not junction_lock:
                count_1110 += 1
                junction_lock = True    # lock further detections
                print("Detected 1110 #", count_1110)
            # Unlock only after junction pattern goes away
            if s != [1,1,1,0]:
                junction_lock = False
            if count_1110 == 7-rackID:
                stop()
                break
            sleep(0.1)
        right_pivot(t=2.7)
    else:
        pass  