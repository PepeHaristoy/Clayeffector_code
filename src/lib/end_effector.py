from lib.DriverCuter0 import DriverCuter0
from lib.DriverCuter1 import DriverCuter1
from lib.DriverCuter2 import DriverCuter2
from machine import Pin, Timer
import time

x = int()

class end_effector:
### we initialize the libraries we made for each motor and we want to
    
    def __init__(self):
        
        self.drv0 = DriverCuter0() # Left extruder motor
        self.drv1 = DriverCuter1() # Right extruder motor
        self.drv2 = DriverCuter2() # cutter motor 
    
    def configure_drivers(self):
        self.drv0.configure_and_report()
        time.sleep(0.5)
        self.drv1.configure_and_report()
        time.sleep(0.5)
        self.drv2.configure_and_report()
        time.sleep(0.5)
        print("All drivers configured and reported.")
    
    def cutter_start_motor(self):
        self.drv2.enableMotor(True)
        time.sleep(0.1)
        
    def cutter_stop_motor(self):
        self.drv2.enableMotor(False)
        time.sleep(0.1)
        
    def cutter_home(self):
        self.drv2.home(50)
        
    """ 
    def cutter_end_position(self):
        self.drv2.home.endHome() - 10 # we make a small offset to avoid hitting the limit switch
        time.sleep(0.1)
        
    def cutter_start_position(self):
        self.drv2.start_position = int(0) + 10 # we make a small offset to avoid hitting the limit switch
        time.sleep(0.1)
    """   
    def cutter_move_to_position_cm(self,position):
        microstepres = self.drv2.tmc.getMicroSteppingResolution()
        self.drv2.move(10*(position * ((microstepres * 200)/8)))
        time.sleep(0.1)
            
    def cutter_move_to_position_mm(self,position):
        microstepres = self.drv2.tmc.getMicroSteppingResolution()
        self.drv2.move(position * ((microstepres * 200)/8))
        time.sleep(0.1)
        
    """   
    def cutter_move_to_open(self):
        self.move_to_position(200)
        time.sleep(0.1)
        
    def cutter_move_to_close(self):
        self.move_to_position(self.end_position - 200)
        time.sleep(0.1)
    """
    
    def extruder_start_motor(self):
            self.drv0.enableMotor(True)
            time.sleep(0.1)
            self.drv1.enableMotor(True)
            time.sleep(0.1)
        
    def extruder_stop_motor(self):
            self.drv0.enableMotor(False)
            time.sleep(0.1)
            self.drv1.enableMotor(False)
            time.sleep(0.1)
            
    def extruder_home(self):
        self.drv0.home(63)
    
    def extruder_move_to_position_cm(self,position):
        microstepres = self.drv0.tmc.getMicroSteppingResolution()
        self.drv0.move(10*(position * ((microstepres * 200)/8)))
        time.sleep(0.1)
        
    def extruder_move_to_position_mm(self,position):
        microstepres = self.drv0.tmc.getMicroSteppingResolution()
        self.drv0.move(position * ((microstepres * 200)/8))
        time.sleep(0.1) 
        """
        self.end_position = int(self.drv0.home.endHome()) - 10 # we make a small offset to avoid hitting the limit switch
        self.start_position = int(0) + 10 # we make a small offset to avoid hitting the limit switch   
        self.lead_screw_total_distance_mm = int((self.end_position - self.start_position)/(self.drv0.t.getmicrosteppingresolution/8))
        self.move_to_position_mm = self.drv0.move(x * (self.drv0.t.getmicrosteppingresolution/8)) # 8 is the screw lead in mm
        self.move_to_steady_position = self.move_to_position_mm(275)
        self.move_to_loading_position = self.move_to_position_mm(285)
        """