import Device as dvc

lys = 0

def set_lys(x):
    global lys
    lys = x
def get_lys():
    return lys

class Light():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    def __init__(self, device):
        self_Device = device
    def run(self):
        set_lys(gpi.analogRead(_Device.get_ConnectorPin()))
        if get_lys() > 10:
            print("Masser af lys")
            #Masser af lys
        if get_lys() < 10:
            TaandLys()

def TaandLys():
    print("Tænder lyset")
