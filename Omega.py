import random

from tango import AttrWriteType, DevState
from tango.server import Device, attribute, command


class Omega(Device):

    Position = attribute(label="Position", dtype=float,
                         access=AttrWriteType.READ_WRITE,
                         fget="get_position", fset="set_position",
                         doc="the omega position")

    def init_device(self):
        # To setUp the state
        Device.init_device(self)
        self.set_state(DevState.ON)

    def get_position(self):
        return random.random()

    def set_position(self, pos):
        print("Setting position to {0}".format(pos))

    @command
    def StopMove(self):
        print("Stopping")


if __name__ == "__main__":
    Omega.run_server()
