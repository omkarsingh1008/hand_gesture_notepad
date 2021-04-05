import cv2
import numpy as np 
import time
import handtracking as htm

import math
wcam,hcam=1200,480
cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime=0

detector=htm.handDetector(detectionCon=0.7)
#from ctypes import cast, POINTER
#from comtypes import CLSCTX_ALL
#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#devices = AudioUtilities.GetSpeakers()
#interface = devices.Activate(
#    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#volrange=volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(0, None)
#minVol=volrange[0]
#maxVol=volrange[1]

l=[]
while True:
	success, img=cap.read()
	img=detector.findHands(img)
	lmList=detector.findPosition(img,draw=False)
	if len(lmList) !=0:
		#print(lmList[4],lmList[8])
		x1,y1=lmList[8][1],lmList[8][2]
		c=[x1,y1]

		#x2,y2=lmList[8][1], lmList[8][2]
		cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
		#cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
		#cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
		#cx,cy=(x1+x2)//2,(y1+y2)//2
		#cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

		#length=math.hypot(x2-x1,y2-y1)
		
		l.append(c)
		if len(l)==2:
			cv2.line(img,(l[0][0],l[0][1]),(l[1][0],l[1][1]),(255,0,255),2)
			del l[0]
			print('hi')

	

		#hand range 50-150
		#voluem raneg -65-0
		#vol=np.interp(length,[50,300],[minVol,maxVol])
		#print(vol)

		#if length <50:
		#	cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)




	cTime=time.time()
	fps=1/(cTime-pTime)
	pTime = cTime

	cv2.putText(img,f'fps:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)


	cv2.imshow("Frame", img)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
cap.release() 