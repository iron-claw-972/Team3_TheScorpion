import time
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

mpu = mpu6050(0x68)

ena=
enb=



GPIO.setmode(GPIO.BOARD)
#GPIO Pins

pin1 = 
pin2 =
pin3 =
pin4 =

GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.output(pin,False)
GPIO.output(pin2,False)
GPIO.output(pin3,False)
GPIO.output(pin4,False)

p=GPIO.PWM(ena, 1000)
p2=GPIO.PWM(enb, 1000)
p.start(ena)
p2.start(enb)

GPIO.setwarnings(False)

firststage = True
secondstage = False
thirdstage = False
counter = 0

gyro = mpu.get_gyro_data()
while (firststage == True):
    ##we can change these numbers later. It is more of a structure.
    #move forward
    p.ChangeDutyCycle(80)#speed
    p2.ChangeDutyCycle(80)#speed
    GPIO.output(pin,False)
    GPIO.output(pin2,True)
    GPIO.output(pin3,False)
    GPIO.output(pin4,True)
    if (gyro['x'] >15 and gyro['x'] < 120):
        firststage = False
        secondstage = True

while (secondstage == True):
    p.ChangeDutyCycle(80)#speed
    p2.ChangeDutyCycle(80)#speed
    GPIO.output(pin,False)
    GPIO.output(pin2,True)
    GPIO.output(pin3,False)
    GPIO.output(pin4,True)
    if (gyro['x'] >0 and gyro['x'] < 15):
        secondstage = False
        thirdstage = True

if (thirdstage == True):
    while (counter <= 20):
        p.ChangeDutyCycle(80)#speed
        p2.ChangeDutyCycle(80)#speed
        GPIO.output(pin,False)
        GPIO.output(pin2,True)
        GPIO.output(pin3,False)
        GPIO.output(pin4,True)

