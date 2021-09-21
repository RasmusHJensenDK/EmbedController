import threading
import Room as rr

temperature = 0

def set_temp(x):
    global temperature
    temperature = x
def get_temp():
    return temperature


class Temperature(threading.Thread):
    _Room = rr.Room(0,0,0)
    def __init__(self, threadID, name, Room):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self._Room = Room
    def run(self):
        [temp, hum] = gpi.dht(tempmoler, 0)
        if self.room._ID == 1:
            if temp > 23:
                set_temp(temp)
                #Throw warning
            if temp < 23: 
                set_temp(temp)
                #Temp is fine
        if self.room_ID == 2:
            if temp > 18:
                set_temp(temp)
                #Throw warning
            if temp < 18:
                set_temp(temp)
                #Temp is fine