import RPi.GPIO as GPIO
import time
MotL_A=5
MotL_B=6
MotR_A=13
MotR_B=19
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)#Trigger Pin
GPIO.setup(24,GPIO.IN)#Echo Pin
GPIO.setup(MotL_A, GPIO.OUT)
GPIO.setup(MotL_B, GPIO.OUT)
GPIO.setup(MotR_A, GPIO.OUT)
GPIO.setup(MotR_B, GPIO.OUT)
t=0
r=0
def Forward():
    GPIO.output(MotL_A, 1)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 1)


def Backward():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 1)
    GPIO.output(MotR_A, 1)
    GPIO.output(MotR_A, 0)


def Left():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 1)


def Right():
    GPIO.output(MotL_A, 1)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 0)


def Stop():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 0)

while True:
    GPIO.output(23,True)
    time.sleep(0.001)
    GPIO.output(23,False)
    while GPIO.input(24)==0:
      t=time.time()
    while GPIO.input(24)==1:
      r=time.time()
    diff=r-t
    d=(34300*diff)/2 
    print int(d)
    if(d < 30):
       Right()
    else:
      Forward()