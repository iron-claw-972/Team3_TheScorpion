import time
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

mpu = mpu6050(0x68)

ena=22
enb=32


GPIO.setmode(GPIO.BOARD)
#GPIO Pins
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.output(18,False)
GPIO.output(16,False)
GPIO.output(26,False)
GPIO.output(24,False)

p=GPIO.PWM(ena, 1000)
p2=GPIO.PWM(enb, 1000)
p.start(22)
p2.start(32)

GPIO.setwarnings(False)

if (gyro_data['x'] == 0){ 
    ##we can change these numbers later. It is more of a structure.
    #move forward
    p.ChangeDutyCycle(80)#speed
    p2.ChangeDutyCycle(80)#speed
    GPIO.output(18,False)
    GPIO.output(16,True)
    GPIO.output(26,False)
    GPIO.output(24,True)
}