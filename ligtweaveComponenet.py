import pylightwaverf

kaku = pylightwaverf.LightWaveRF()

def sendValueToLamp(val):

    kaku_val = (int(val)/3)-1
    if kaku_val <1:
        kaku_val = 1
    kaku.test_control(kaku_val)

def register():
    kaku.register_device()
