import enum
import Room as rr
import Device as dvc

class Devices():
    _TempDevices = []
    _SoundDevices = []
    _LightDevices = []
    _Rooms = []

    def __init__(self):
        City_Ground_floor_South = rr.Room(1,1,1)
        City_Ground_floor_Center = rr.Room(2,1,2)
        City_Ground_floor_North = rr.Room(3,1,3)

        City_First_Floor_South = rr.Room(4,1,4)
        City_First_Floor_Center = rr.Room(5,1,5)
        City_First_Floor_North = rr.Room(6,1,6)

        self._Rooms.append(City_Ground_floor_South)
        self._Rooms.append(City_Ground_floor_Center)
        self._Rooms.append(City_Ground_floor_North)

        self._Rooms.append(City_First_Floor_South)
        self._Rooms.append(City_First_Floor_Center)
        self._Rooms.append(City_First_Floor_North)

        City_Device_Ground_Floor_South_Temperature = dvc.Device(7, "Ground Floor South Temperature", City_Ground_floor_South, "OFF")
        City_Device_Ground_Floor_South_Light = dvc.Device(15, "Ground Floor South Light", City_Ground_floor_South, "OFF")
        City_Device_Ground_Floor_South_Sound = dvc.Device(14, "Ground Floor South Sound", City_Ground_floor_South, "OFF")

        City_Device_Ground_Floor_Center_Temperature = dvc.Device(7, "Ground Floor Center Light", City_Ground_floor_Center, "OFF")
        City_Device_Ground_Floor_Center_Light = dvc.Device(15, "Ground Floor Center Light", City_Ground_floor_Center, "OFF")
        City_Device_Ground_Floor_Center_Sound = dvc.Device(14, "Ground Floor Center Sound", City_Ground_floor_Center, "OFF")

        City_Device_Ground_Floor_North_Temperature = dvc.Device(7, "Ground Floor North Temperature", City_Ground_floor_North, "OFF")
        City_Device_Ground_Floor_North_Light = dvc.Device(15, "Ground Floor North Light", City_Ground_floor_North, "OFF")
        City_Device_Ground_Floor_North_Sound = dvc.Device(14, "Ground Floor North Sound", City_Ground_floor_North, "OFF")

        self._TempDevices.append(City_Device_Ground_Floor_South_Temperature)
        self._TempDevices.append(City_Device_Ground_Floor_Center_Temperature)
        self._TempDevices.append(City_Device_Ground_Floor_North_Temperature)

        self._LightDevices.append(City_Device_Ground_Floor_South_Light)
        self._LightDevices.append(City_Device_Ground_Floor_Center_Light)
        self._LightDevices.append(City_Device_Ground_Floor_North_Light)

        self._SoundDevices.append(City_Device_Ground_Floor_South_Sound)
        self._SoundDevices.append(City_Device_Ground_Floor_Center_Sound)
        self._SoundDevices.append(City_Device_Ground_Floor_North_Sound)

        City_Device_First_Floor_South_Temperature = dvc.Device(7, "First Floor South Temperature", City_First_Floor_South, "OFF")
        City_Device_First_Floor_South_Light = dvc.Device(15, "First Floor South Light", City_First_Floor_South, "OFF")
        City_Device_First_Floor_South_Sound = dvc.Device(14, "First Floor South Sound", City_First_Floor_South, "OFF")

        City_Device_First_Floor_Center_Temperature = dvc.Device(7, "First Floor Center Light", City_First_Floor_Center, "OFF")
        City_Device_First_Floor_Center_Light = dvc.Device(15, "First Floor Center Light", City_First_Floor_Center, "OFF")
        City_Device_First_Floor_Center_Sound = dvc.Device(14, "First Floor North Sound", City_First_Floor_Center, "OFF")

        City_Device_First_Floor_North_Temperature = dvc.Device(7, "First Floor North Temperature", City_First_Floor_North, "OFF")
        City_Device_First_Floor_North_Light = dvc.Device(15, "First Floor North Light", City_First_Floor_North, "OFF")
        City_Device_First_Floor_North_Sound = dvc.Device(14, "First Floor North Sound", City_First_Floor_North, "OFF")

        self._TempDevices.append(City_Device_First_Floor_South_Temperature)
        self._TempDevices.append(City_Device_First_Floor_Center_Temperature)
        self._TempDevices.append(City_Device_First_Floor_North_Temperature)

        self._LightDevices.append(City_Device_First_Floor_South_Light)
        self._LightDevices.append(City_Device_First_Floor_Center_Light)
        self._LightDevices.append(City_Device_First_Floor_North_Light)

        self._SoundDevices.append(City_Device_First_Floor_South_Sound)
        self._SoundDevices.append(City_Device_First_Floor_Center_Sound)
        self._SoundDevices.append(City_Device_First_Floor_North_Sound)


class main():
    #next((x for x in self._SoundDevices if x.Type == "SomeType"), None)
    _DATA = Devices()
    _RoomIDToExamine = 0
    _RoomDevicesToExamine = []
    buildingInput = input("Building Nr.? :")
    RoomInput = input("Room nr.? :")

    for x in _DATA._Rooms:
        if str(x.get_building()) == str(buildingInput):
            if str(x.get_number()) == str(RoomInput):
                _RoomIDToExamine = x.get_id()

    for x in _DATA._LightDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)
    for x in _DATA._SoundDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)
    for x in _DATA._TempDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)
    

main()