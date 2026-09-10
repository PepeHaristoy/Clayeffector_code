from lib.end_effector import end_effector
from machine import Pin, Timer
import time
# we define the values to use in the code
input_cutter = None
input_extruder = None
iter_count = 0
a=(Pin(2, Pin.IN, Pin.PULL_DOWN))
b=(Pin(2, Pin.IN, Pin.PULL_DOWN))
c=(Pin(2, Pin.IN, Pin.PULL_DOWN))
d=(Pin(2, Pin.IN, Pin.PULL_DOWN))
e=(Pin(2, Pin.IN, Pin.PULL_DOWN))

effector = end_effector()

### we define the functions to use in the code
def read_robot_inputs(a,b,c,d):
    global input_cutter
    global input_extruder
    if a.value() == 1:
        input_cutter = 1
    elif b.value() == 1:
        input_cutter = 2
    elif c.value() == 1:
        input_extruder = 1  
    elif d.value() == 1:
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
def secuencia_move_extruder(input_extruder, iter_count):

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
while e == 1:
    read_robot_inputs(a,b,c,d)

    if input_cutter is not None:
        secuencia_move_cutter(input_cutter)
        input_cutter = None
    elif input_extruder is not None:
        secuencia_move_extruder(input_extruder, iter_count)
        input_extruder = None
        iter_count += 1
    else:
        continue
"""


### recuperar movimiento
from lib.TMC_2209_StepperDriver import TMC_2209
motor = TMC_2209(12, 11, 10, Pin(17), Pin(16),mtr_id=0)
motor.setCurrentPosition(6750)
### primer movimiento cutter a posición de medicion de extrusor

effector.cutter_start_motor()
effector.cutter_home()
effector.cutter_stop_motor()

effector.cutter_start_motor()
effector.cutter_move_to_position_cm(0)
effector.cutter_stop_motor()

effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()

effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()

### empieza extrusor autohome
effector.extruder_start_motor()
effector.extruder_home()
effector.extruder_stop_motor()

effector.extruder_start_motor()
effector.extruder_move_to_position_mm(280)
effector.extruder_stop_motor()

### se abre el cutter
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(7)
effector.cutter_stop_motor()

### empieza a extruir el tubo
effector.extruder_start_motor()
effector.extruder_move_to_position_mm(210)
effector.extruder_stop_motor()
### corte cierra el cutter
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()
### se abre el cutter
time.sleep(2)
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(9)
effector.cutter_move_to_position_cm(9)
effector.cutter_stop_motor()
### empieza a extruir el tubo
effector.extruder_start_motor()
effector.extruder_move_to_position_mm(140)
effector.extruder_stop_motor()
### corte cierra el cutter
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()
### se abre el cutter
time.sleep(2)
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(9)
effector.cutter_move_to_position_cm(9)
effector.cutter_stop_motor()
### empieza a extruir el tubo
effector.extruder_start_motor()
effector.extruder_move_to_position_mm(70)
effector.extruder_stop_motor()
### corte cierra el cutter
time.sleep(4)
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()
### se abre el cutter
time.sleep(2)
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(9)
effector.cutter_move_to_position_cm(9)
effector.cutter_stop_motor()
### empieza a extruir el tubo
effector.extruder_start_motor()
effector.extruder_move_to_position_mm(3)
effector.extruder_stop_motor()
### corte cierra el cutter
effector.cutter_start_motor()
effector.cutter_move_to_position_cm(1)
effector.cutter_move_to_position_cm(1)
effector.cutter_stop_motor()

"""