class Aircraft:
    callsign: str
    position: (x,y)
    altitude: int
    attitude: (pitch,yaw,roll)
    heading : int
    airspeed: int
    landing_heading: int
    landing_heading: int
    type: str
    destination: str
    flight_path: curve

class Waypoint:
    name: str
    position: (x,y)
    type: str

class Airport:
    name: str
    position: (x,y)
    altitude: int
    runway_details: list{runway}
    wind_details: list{timer:list{speed}}

class Game_State:
    list_Planes: list[Aircraft]
    list_Waypoints: list[Waypoint]
    list_Airport: list[Airport]
    score:int
    time: float
    commands: action

    int x,y 
    int pitch,yaw,roll
    runway = {}
    timer = {speed}
    speed = {indication:}
