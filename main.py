from lib.end_effector import end_effector
from machine import Pin, Timer
import time

effector = end_effector()


### we define the inputs pins and the output pin for the robot arm
effector.configure_drivers()
time.sleep(1)
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