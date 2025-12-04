from led import enableYellowLED, disableYellowLED
from navigation import navigateStartBoxToLeftRowFirstRackEntry, navigateFromLeftRowToRightRowFirstRackEntry,\
    goToRackEntrance, deliverFromRack, moveToPreviousRackEntry, navigateFromCurrentRackEntryToStartBox
from rackScan import scanBottomLevel, scanTopLevel
import state
from button import isButtonPressed
from utime import sleep

MAX_RACK_ID = 6
MIN_RACK_ID = 1
DELIVERIES_FOR_RETURN = 4

def scanOneRow(side):
    if side == 'Left':
        navigateStartBoxToLeftRowFirstRackEntry()
        # A6, facing rack
    else:
        navigateFromLeftRowToRightRowFirstRackEntry()
        # B6, facing rack
    state.rackCursor = MAX_RACK_ID     # 6
    state.currentRackPos = MAX_RACK_ID
    state.level = 'BOTTOM'               # check 'BOTTOM' level first
    state.justReturnedBottom = False
    state.side = side

    # Main loop — scan racks until finished
    while state.rackCursor >= MIN_RACK_ID and state.deliveredCount < DELIVERIES_FOR_RETURN:
        if state.level == 'BOTTOM':
            if state.justReturnedBottom == True:
                state.justReturnedBottom = False
                state.level = 'TOP'
                continue # skip bottom scan & go to top scan
            goToRackEntrance(state.rackCursor, side)   # ensure at rack entrance, facing rack
            found, color = scanBottomLevel(state.rackCursor) 
            if found:
                # has box on bottom level, deliver and return to same rack entry
                deliverFromRack(state.rackCursor, color, side) 
                state.deliveredCount += 1
                state.justReturnedBottom = True
            else:
                state.level = 'TOP'

        else:   # TOP LEVEL
            # goToRackEntrance(state.rackCursor, side)
            # found, color = scanTopLevel(state.rackCursor)
            # if found:
            #     deliverFromRack(state.rackCursor, color,side)
            #     state.deliveredCount += 1
            # if state.rackCursor == MIN_RACK_ID:
            #     # finished scanning this row
            #     break
            moveToPreviousRackEntry(state.rackCursor, side) 
            state.rackCursor -= 1
            state.level = 'BOTTOM'
            state.justReturnedBottom = False
while True:
    # --- Wait for press ---
    if isButtonPressed():
        print("Button pressed! Starting robot.")
        break
    sleep(0.05)
enableYellowLED() 
sleep(0.25)  # debounce
# --- RUN TASK ---
print("Starting Robot Task")
scanOneRow('Left')
if state.deliveredCount < DELIVERIES_FOR_RETURN:
    scanOneRow('Right')
navigateFromCurrentRackEntryToStartBox(state.side)
disableYellowLED()
print("Task completed!")

 
