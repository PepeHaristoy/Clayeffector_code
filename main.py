from lib.end_effector import end_effector
from machine import Pin
import time
# we define the values to use in the code
input_cutter = None
input_extruder = None

iter_count = 0
effector = end_effector()

a=(Pin(18, Pin.IN, Pin.PULL_UP))
b=(Pin(19, Pin.IN, Pin.PULL_UP))
c=(Pin(20, Pin.IN, Pin.PULL_UP))
d=(Pin(21, Pin.IN, Pin.PULL_UP))

enable=(Pin(22, Pin.IN, Pin.PULL_UP))
action_ended=(Pin(26, Pin.OUT, value=0))


### we define the functions to use in the code
def read_robot_inputs(a,b,c,d):
    global input_cutter , input_extruder
    input_cutter = None
    input_extruder = None
    
    if a.value() == 0:
        input_cutter = 1
    elif b.value() == 0:
        input_cutter = 2
    elif c.value() == 0:
        input_extruder = 1  
    elif d.value() == 0:
        input_extruder = 2  
    else:
        input_cutter = None
        input_extruder = None

### we define home functions for cutter and extruder
def secuencia_home_cutter():
    effector.cutter_start_motor()
    effector.cutter_home()
    effector.cutter_stop_motor()

def secuencia_home_extruder():
    effector.extruder_start_motor()
    effector.extruder_home()
    effector.extruder_stop_motor()

### we define the functions to move the cutter and extruder
def secuencia_move_cutter(input_cutter):
    if input_cutter ==1:
        effector.cutter_start_motor()
        effector.cutter_move_to_position_cm(0)
        effector.cutter_stop_motor()
    elif input_cutter ==2:
        effector.cutter_start_motor()
        effector.cutter_move_to_position_cm(6)
        effector.cutter_stop_motor()
    else:
        return None
### 
def secuencia_move_extruder(input_extruder):
    global iter_count

    if input_extruder == 1:
        effector.extruder_start_motor()
        effector.extruder_move_to_position_mm(280)
        effector.extruder_stop_motor()
        iter_count = 0

    elif input_extruder == 2 and iter_count ==1:
        effector.extruder_start_motor()
        effector.extruder_move_to_position_mm(210)
        effector.extruder_stop_motor()
    elif input_extruder == 2 and iter_count ==2:
        effector.extruder_start_motor()
        effector.extruder_move_to_position_mm(140)
        effector.extruder_stop_motor()
    elif input_extruder == 2 and iter_count ==3:
        effector.extruder_start_motor()
        effector.extruder_move_to_position_mm(70)
        effector.extruder_stop_motor()
    elif input_extruder == 2 and iter_count ==4:
        effector.extruder_start_motor()
        effector.extruder_move_to_position_mm(3)
        effector.extruder_stop_motor()
    else:
        return None

### we start the configuration of the drivers
effector.configure_drivers()
time.sleep(1)
secuencia_home_cutter()
secuencia_home_extruder()
### we define the main loop to use in the code waiting for input

while True:
    if enable.value() == 0:
        read_robot_inputs(a,b,c,d)
        time.sleep(0.1)
        print("input_cutter: ", input_cutter, "input_extruder: ", input_extruder)

        if input_cutter is not None:
            secuencia_move_cutter(input_cutter)
            action_ended.value(1)
            time.sleep(0.1)
            action_ended.value(0)
            input_cutter = None

        elif input_extruder is not None:
            secuencia_move_extruder(input_extruder)
            action_ended.value(1)
            time.sleep(0.1)
            action_ended.value(0)
            input_extruder = None
            iter_count += 1
    else:
        time.sleep(0.1)