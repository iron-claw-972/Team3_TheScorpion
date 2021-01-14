
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

mpu = mpu6050(0x68)

ena=18
enb=12



GPIO.setmode(GPIO.BCM)
#GPIO Pins

GPIO.setwarnings(False)

pin1 = 4
pin2 = 17
pin3 = 27
pin4 = 22

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.output(pin1,False)
GPIO.output(pin2,False)
GPIO.output(pin3,False)
GPIO.output(pin4,False)

p=GPIO.PWM(ena, 1000)
p2=GPIO.PWM(enb, 1000)
p.start(ena)
p2.start(enb)



firststage = True
secondstage = False
thirdstage = False
counter = 0

p.ChangeDutyCycle(80)#speed
p2.ChangeDutyCycle(80)#speed
GPIO.output(pin1,True)
GPIO.output(pin2,False)
GPIO.output(pin3,True)
GPIO.output(pin4,False)

while (firststage == True):
    ##we can change these numbers later. It is more of a structure.
    #move forward
    accel_data = mpu.get_accel_data()
    if (accel_data['y'] > 4):
        firststage = False
        secondstage = True
        print("moving to second")
    
while (secondstage == True):
    accel_data = mpu.get_accel_data()
    if (accel_data['y'] < 3):
        print("moving to third")
        secondstage = False
        thirdstage = True

while (thirdstage == True):
    while (counter <= 20):
        print("3rd")
        counter += 1
    thirdstage = False
p.ChangeDutyCycle(80)#speed
p2.ChangeDutyCycle(80)#speed
GPIO.output(pin1,False)
GPIO.output(pin2, False)
GPIO.output(pin3,False)
GPIO.output(pin4, False)