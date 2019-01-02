#!/usr/bin/env python2

import tango

from sardana.pool.controller import MotorController

TANGO_DEV = 'device/motor/omega'


class FourChannel(MotorController):

    def __init__(self, inst, props):
        print "__init__"
        MotorController.__init__(self, inst, props)
        self.mydevice = tango.DeviceProxy(TANGO_DEV)
        self.mydevice.command_inout("Init")

    def AddDevice(self, axis):
        print "AddDevice"

    def StateOne(self, axis):
        print "StateOne"
        return (self.mydevice.state(), self.mydevice.status())

    def ReadOne(self,axis):
        print "ReadOne"
        return self.mydevice.Position

    def StartOne(self, axis, position):
        print "StartOne"
        self.mydevice.Position = position
        return

    def StopOne(self, axis, position):
        print "StopOne"
        self.mydevice.command_inout("StopMove")
        return

    def AbortOne(self, axis):
        print "AbortOne"
        self.mydevice.command_inout("StopMove")
        return
