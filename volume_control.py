import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

##############################
widthcamera,heightcamera=640,480
ctime=0
ptime=0
vol=0
volBar=400
volPer=0
##############################


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
minVolume=volRange[0]
maxVolume=volRange[1]






capture=cv2.VideoCapture(0)
capture.set(3,widthcamera)
capture.set(4,heightcamera)
detector=htm.HandDetector()
while True:
    success,image=capture.read()
    image=detector.findHands(image)
    lmlist=detector.findPosition(image,draw= False)
    if len(lmlist)!=0:
        # print(lmlist[4],lmlist[8])

        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2


        cv2.circle(image,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(image, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(image,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(image, (cx,cy), 15, (255, 0, 255), cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        # print(length)
        #hand range 10 to 180
        #volume range -63 to 0
        vol=np.interp(length,[10,180],[minVolume,maxVolume])
        volPer=np.interp(length,[50,300],[0,100])
        volBar=np.interp(length,[50,300],[400,150])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length<15:
            cv2.circle(image, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(image,(50,150),(85,400),(255,0,0),3)
    cv2.rectangle(image, (50, (int(volBar))), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(image,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),2)
    cv2.imshow('Result',image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break