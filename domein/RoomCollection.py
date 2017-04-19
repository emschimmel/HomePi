from domein.Room import Room
from domein.Device_Type_Lamp import Device_Type_Lamp
from domein.Device_Type_Lyric import Device_Type_Lyric
from domein.Device_Type_Music import Device_Type_Music

#--------------------------------------------------------------
#   at a later state: get the struct from the kaku server
#   then enridge with own config.
#--------------------------------------------------------------
class RoomCollection():

    SELECTEDROOM_DEFAULTVALUE = Room('Hallway', [])
    ROOMCOLLECTION = [
        [
            Room('Livingroom', [
                Device_Type_Lamp(1, 1, "Lamp"),
                Device_Type_Lyric(1, 2, "Termostaat")
            ])
        ],
        [
            Room('Bedroom', [
                Device_Type_Lamp(2, 1, "Lamp")
            ]),
            Room('Library', [
                Device_Type_Lamp(3, 1, "Lamp"),
                Device_Type_Music(3, 2, "Radio")
            ]),
            Room('Childroom', [
                Device_Type_Lamp(4, 1, "MooiLamp")
            ])
        ]
    ]

    def __init__(self):
        self._build_collection()

    def _build_collection(self):
        self.ROOMCOLLECTION   = self.ROOMCOLLECTION

