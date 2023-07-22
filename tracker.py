import cv2
import sys
import serial
import time


# u=false 

ser = serial.Serial('COM3') # COMxx   format on Windows
                                   # ttyUSBx format on Linux

ser.baudrate = 9600  # set Baud rate to 9600
ser.bytesize = 8     # Number of data bits = 8
ser.parity   ='N'    # No parity
ser.stopbits = 1     # Number of Stop bits = 1
time.sleep(3)
uSend = False
sSend = False
dSend = False

lSend = False
ssSend = False
rSend = False
# for i in range(5) :
#     SerialObj.write(b'A')      #transmit 'A' (8bit) to micro/Arduino

# def writeSerial(x):
#    arduino.write(bytes(x))
#    #qarduino.write(x))
#  
#   time.sleep(0.05)
#    #  data = arduino.readline()
   #  return data

#import pyautogui

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
print(cv2.__version__)

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use

   tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
   tracker_type = tracker_types[6]

    # tracker = cv2.legacy.TrackerMOSSE_create()

   tracker = cv2.TrackerCSRT_create()
        

    # if int(major_ver) < 4 and int(minor_ver) < 3:
    #     tracker = cv2.cv2.Tracker_create(tracker_type)
    # else:
    #     # if tracker_type == 'BOOSTING':
        #     tracker = cv2.TrackerBoosting_create()
        # if tracker_type == 'MIL':
        #     tracker = cv2.TrackerMIL_create()
        # if tracker_type == 'KCF':
        #     tracker = cv2.TrackerKCF_create()
        # if tracker_type == 'TLD':
        #     tracker = cv2.TrackerTLD_create()
        # if tracker_type == 'MEDIANFLOW':
        #     tracker = cv2.TrackerMedianFlow_create()
        # if tracker_type == 'CSRT':
        #     tracker = cv2.TrackerCSRT_create()
        # if tracker_type == 'MOSSE':
        #     tracker = cv2.legacy.TrackerMOSSE_create()

    # Read video
   video = cv2.VideoCapture(1)


    # Read first frame.
   ok, frame = video.read()
    # print(ok)

    # Define an initial bounding box
   bbox = (287, 23, 86, 320)

    # Uncomment the line below to select a different bounding box
   bbox = cv2.selectROI(frame, True)

    # Initialize tracker with first frame and bounding box
   ok = tracker.init(frame, bbox)

   while True:
     # Read a new frame
      ok, frame = video.read()
      # height, width = frame.shape[:2]
      # print("height:" , height)
      # print("width:" , width)

     # Start timer
      timer = cv2.getTickCount()

     # Update tracker
      ok, bbox = tracker.update(frame)

     # Calculate Frames per second (FPS)
      fps  = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        
     # Draw bounding box
      if ok:
      # Tracking success
         p1 = (int(bbox[0]), int(bbox[1]))
         p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
         cv2.rectangle(frame, p1, p2, (255,255,0), 2, 1)
         x = (p1[0] + p2[0])/2
         y = (p1[1] + p2[1])/2



         # print('y =' , y)
         #ser.write(x.encode())      #transmit 'A' (8bit) to micro/Arduino
         # ser.write((str(x) + 'a').encode('utf-8'))
         if x > 350 :
            if rSend == False :
               rSend = True
               lSend = False
               ssSend = False
               print('x1 =' , x)
               ser.write(('r').encode('utf-8'))
               # ser.write(('u').encode('utf-8'))
         elif x < 250 :
            if lSend == False :
               lSend = True
               rSend = False
               ssSend = False  
               print('x3 =' , x)
               ser.write(('l').encode('utf-8'))
            # ser.write(('d').encode('utf-8'))
         elif x>250 and x<350 :
            if ssSend == False :
               ssSend = True
               lSend = False
               rSend = False  
               print('x2 =' , x)
               ser.write(('x').encode('utf-8'))

         if y > 300 :
            if uSend == False :
               uSend = True
               dSend = False
               sSend = False
               print('y1 =' , y)
               ser.write((str(x) + 'u').encode('utf-8'))
               # ser.write(('u').encode('utf-8'))
         elif y < 200 :
            if dSend == False :
               dSend = True
               uSend = False
               sSend = False  
               print('y3 =' , y)
               ser.write(('d').encode('utf-8'))
            # ser.write(('d').encode('utf-8'))
         else :
            if sSend == False :
               sSend = True
               uSend = False
               dSend = False  
               print('y2 =' , y)
               ser.write(('s').encode('utf-8'))
            # ser.write(('s').encode('utf-8'))
         

         

         
         # ser.write((str(y) + 'a').encode('utf-8'))
         
         #print((str(x) + 'a').encode('utf-8'))
            #
            # print('y =' , y)
   


      else :
            # Tracking failure
         cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

     # Display tracker type on frame
    #  cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
  
     # Display FPS on frame
    #  cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
     # Display result
      cv2.imshow("Tracking", frame)

     # Exit if ESC pressed
      if cv2.waitKey(1) & 0xFF == ord('q'): # if press SPACE bar
         break

video.release()
cv2.destroyAllWindows()