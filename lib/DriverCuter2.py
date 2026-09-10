from lib.TMC_2209_StepperDriver import *
import time
from machine import Pin


##p Las primeras piezas de este codigo es una iniciación segmentada para poder hacer debugging
##p vamos a partir con la definición de parametros relevantes para el uart
#initiate the TMC_2209 class
# use your pins for pin_step, pin_dir, pin_en, pin_rx, pin_tx, mtr_id (defined by MS1 and MS2 pins) here
class DriverCuter2:
    def __init__(self):
        
        self.endHome = 0
        MS1Pin = Pin(11,Pin.OUT)
        MS2Pin = Pin(10,Pin.OUT)
        MS1Pin.value(0)
        MS2Pin.value(0)
        self.tmc = TMC_2209(15, 14, 13, Pin(1), Pin(0),mtr_id=2)
        #we have to keep the motor off until we need it
        
    def configure_and_report(self):
        t = self.tmc

        ### First we configure the debug config
        t.setLoglevel(Loglevel.info)
        #     none = 0
        #     error = 10
        #      info = 20
        #     debug = 30
        #     movement = 40
        #     all = 100

        ### then we configure the driver power
        print("IScaleAnalog = " + str(t.getIScaleAnalog()))   # we should expect a 1
        print("InternalRsense = " + str(t.getInternalRSense()))   # we should expect a 1
        t.setCurrent(500)
        
        ### then we go with stepping config
        t.setSpreadCycle(False) #stealthchop
        print(t.getInterpolation())
        t.setMicroSteppingResolution(1)
        print(t.getMicroSteppingResolution())
        print(t.readStepsPerRevolution())
        
        ### then we configure the maximal speed and acceleration
        t.setMovementAbsRel(MovementAbsRel.absolute)
        t.setDirection_reg(False)
        t.setAcceleration(2000)
        t.setMaxSpeed(400)
        

        ###finally we read the current settings in the TMC register
        print("---\n---")
        t.readIOIN()
        t.readCHOPCONF()
        t.readDRVSTATUS()
        t.readGCONF()
        print("---\n---")
        
    def enableMotor(self,en):
        t = self.tmc
        t.setMotorEnabled(en)
        
    def move(self,steps):
        t = self.tmc
        time.sleep(0.1)
        t.runToPositionSteps(steps)
        time.sleep(0.1)
        
    def home(self,threshold):
        t = self.tmc
        
        def my_callback(channel):  
            print("StallGuard!")
            t.stop()
            
        t.setStallguard_Callback(4, threshold, my_callback) # after this function call, StallGuard is active
        finishedsuccessfully = t.runToPositionSteps(-4000, MovementAbsRel.relative)    #move 4000 steps forward
        if(finishedsuccessfully == True):
            print("Movement finished successfully")
        else:
            print("Movement was not completed")
        
        t.setCurrentPosition(0)

        t.setStallguard_Callback(4, threshold, my_callback) # after this function call, StallGuard is active
        finishedsuccessfully = t.runToPositionSteps(4000, MovementAbsRel.relative)    #move 4000 steps forward
        if(finishedsuccessfully == True):
            print("Movement finished successfully")
        else:
            print("Movement was not completed")
        
        t.setStallguard_Callback(4, threshold, my_callback)
        
        print(t.getCurrentPosition())
        self.endHome = int(t.getCurrentPosition())