from domein.Room import Room
from domein.Device import Device

#--------------------------------------------------------------
#   at a later state: get the struct from the kaku server
#   then enridge with own config.
#--------------------------------------------------------------
class RoomCollection():

    SELECTEDROOM_DEFAULTVALUE = Room('Hallway', [])
    ROOMCOLLECTION = [
        [
            Room('Livingroom', [
                Device(1, 1, "lamp", "Lamp"),
                Device(1, 2, "lamp", "StaLamp")
            ])
        ],
        [
            Room('Bedroom', [
                Device(2, 1, "lamp", "Lamp")
            ]),
            Room('Library', [
                Device(3, 1, "lamp", "Lamp")
            ]),
            Room('Childroom', [
                Device(4, 1, "lamp", "MooiLamp")
            ])
        ]
    ]

    def __init__(self):
        self._build_collection()

    def _build_collection(self):
        self.ROOMCOLLECTION   = self.ROOMCOLLECTION

