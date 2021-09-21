import threading
import Room as rr
import Device as dvc

sound = 0

def set_sound(x):
    global sound
    sound = x
def get_sound():
    return sound

class SoundCheck(threading.Thread):
    _Room = rr.Room(0,0,0)
    _Device = dvc.Device(0,"NaN",0,"OFF")
    def __init__(self, threadID, name, room, device):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self._Room = room
        self._Device = device
    def run(self):
        while True:
            sound_level = gpi.analogRead(_Device.get_ConnectorPin())
            if sound_level > 600:
                #Throw warning sound level too high
                set_sound(sound_level)
            else:
                set_sound(sound_level)