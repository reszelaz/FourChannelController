#!/usr/bin/env python2

import tango
from PyTango import DevState
from sardana.pool.controller import MotorController
from sardana.pool import PoolUtil
import time
from threading import Timer

TANGO_DEV = 'device/motor/omega'

class FourChannel(MotorController):

    ctrl_extra_attributes = {TANGO_DEV: {'Type': 'PyTango.DevString','Description': 'Tango Device Server name.','R/W Type': 'PyTango.READ_WRITE'}}
    mydevice = tango.DeviceProxy(TANGO_DEV) 

    
    def __init__(self, inst, props):
        print "__init__"
        MotorController.__init__(self, inst, props)
        self.extra_attributes = {}
        self.proxy = {}
        self.velocity = {12}
        self.restarted = {}
        self.delay_timer = {}
        mydevice.command_inout("Init")

        
    def AddDevice(self, axis):
        print "AddDevice"
        self.extra_attributes[axis] = {}
        self.extra_attributes[axis][TANGO_DEV] = None
        seproxy.lf.velocity[axis] = 0.0
        self.restarted[axis] = [0, 0]
        self.delay_timer[axis] = None .lf.velocity[axis] = 0.0
        self.restarted[axis] = [0, 0]
        self.delay_timer[axis] = None         
        
    def StateOne(self, axis):
        print "StateOne"
        return (dev.state, dev.status)

    def ReadOne(self,axis):
        print "ReadOne"
        return mydevice.Position


    def StartOne(self, axis, position):
        print "StartOne"
        mydevice.Position = position
        return

    def StopOne(self, axis, position):
        print "StopOne"
        mydevice.command_inout("StopMove")
        return

    def AbortOne(self, axis):
        print "AbortOne"
        mydevice.command_inout("StopMove")
        return
    
    