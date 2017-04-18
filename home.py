import Tkinter as tk
from RoomCollection import RoomCollection
try:
    from pylightwaverf import LightWaveRF as kaku # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'ligtweaveComponenet.py' in the directory containing %r. \n" % __file__)
    sys.exit(1)

#--------------------------------------------------------------
#   global vars
#--------------------------------------------------------------
selectedroom_defaultvalue = RoomCollection.SELECTEDROOM_DEFAULTVALUE
selectedroom = selectedroom_defaultvalue
selectedfloor = 1
testJSONCollection = RoomCollection.ROOMCOLLECTION
#--------------------------------------------------------------
#   window
#--------------------------------------------------------------
w = 640
h = 320
heightbuttonrow = 30
root = tk.Tk()
root.title('home')
root.geometry("%dx%d+%d+%d" % (w, h, 0, 0))

# buttons top
staticbuttonrow = tk.Frame(root)
staticbuttonrow.place(y=0,x=0)

buttonrow = tk.Frame(root)
buttonrow.place(y=0,x=270)

#main frame
mainwindow = tk.Frame(root)
mainwindow.place(y=heightbuttonrow,x=0, width=w, height=(h-heightbuttonrow))

#--------------------------------------------------------------
#   button actions
#--------------------------------------------------------------
def selectroom(room):
    global selectedroom
    selectedroom = room

    drawfloorcontent()
    currentx = 0
    for lam in room.roomConfigCollection:
        if lam.typedevice is 'lamp':
            drawLampSlider(lam, currentx)
            currentx+=160
        elif lam.typedevice is 'music':
            drawMusicbox(lam, currentx)
            currentx+=250

def switchfloor():
    global selectedfloor

    if selectedfloor == 1:
        selectedfloor = 0
    else:
        selectedfloor = 1
    selectroom(selectedroom_defaultvalue)
    drawbuttonsforfloor()
    drawfloorcontent()

#--------------------------------------------------------------
#   private functions
#--------------------------------------------------------------
def drawstaticbuttons():
    button = tk.Button(staticbuttonrow, text='Close', command = lambda: root.destroy())
    button.pack(side='left')
    button = tk.Button(staticbuttonrow, text='Register pi', command = lambda: kaku.register_device())
    button.pack(side='left',)
    button = tk.Button(staticbuttonrow, text='Switch floor', command = lambda: switchfloor())
    button.pack(side='left',)


def drawfloorcontent():
    for widget in mainwindow.winfo_children():
        widget.destroy()

    headerlabelcontrol = tk.Frame(mainwindow)
    headerlabelcontrol.place(y=0,x=0, width=w)
    label = tk.Label(headerlabelcontrol, text=selectedroom.name, fg = "white", bg = "purple", font = "Helvetica 16 bold", width=w)
    label.pack()


def drawbuttonsforfloor():
    for widget in buttonrow.winfo_children():
        widget.destroy()

    #dynamic
    for currentroom in testJSONCollection[selectedfloor]:
        button = tk.Button(buttonrow, text=currentroom.name, command = (lambda currentroom=currentroom: lambda: selectroom(currentroom))())
        button.pack(side='left',)

#--------------------------------------------------------------
#   lambda draw functions
#--------------------------------------------------------------
def drawLampSlider(device_config, currentx):

    labelcontrol = tk.Frame(mainwindow)
    labelcontrol.place(y=30,x=currentx, width=150)
    label = tk.Label(labelcontrol, text=device_config.name, fg = "white", bg = "dark grey", font = "Helvetica 16 bold", width=250)
    label.pack()

    slidecontrol = tk.Frame(mainwindow)
    slidecontrol.place(y=65,x=currentx+100, width=50)
    slider = tk.Scale(slidecontrol, from_=0, to=100, command = lambda value, device_config=device_config: device_config.sendValueToLampBySlider(value))
    slider.pack(side='left')

    buttoncontrol = tk.Frame(mainwindow)
    buttoncontrol.place(y=65,x=currentx, width=100)
    button = tk.Button(buttoncontrol, text='Off', command = lambda: device_config.sendValueLampOff(slider), width=100)
    button.pack()
    button = tk.Button(buttoncontrol, text='25%', command = lambda: device_config.sendValueToLamp(25, slider), width=100)
    button.pack()
    button = tk.Button(buttoncontrol, text='50%', command = lambda: device_config.sendValueToLamp(50, slider), width=100)
    button.pack()
    button = tk.Button(buttoncontrol, text='75%', command = lambda: device_config.sendValueToLamp(75, slider), width=100)
    button.pack()
    button = tk.Button(buttoncontrol, text='100%', command = lambda: device_config.sendValueToLamp(100, slider), width=100)
    button.pack()
    button = tk.Button(buttoncontrol, text='On', command = lambda: device_config.sendValueLampOn(slider), width=100)
    button.pack()

def drawMusicbox(device_config, currentx):
    labelcontrol = tk.Frame(mainwindow)
    labelcontrol.place(y=30,x=currentx, width=150)
    label = tk.Label(labelcontrol, text=device_config.name, fg = "white", bg = "dark grey", font = "Helvetica 16 bold", width=250)
    label.pack()

#--------------------------------------------------------------
#   run
#--------------------------------------------------------------
drawstaticbuttons()
drawbuttonsforfloor()
drawfloorcontent()
root.mainloop()
