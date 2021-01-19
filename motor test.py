
import RPi.GPIO as GPIO   
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

GPIO.output(pin1,True)
GPIO.output(pin2,False)
GPIO.output(pin3,True)
GPIO.output(pin4,False)

p=GPIO.PWM(ena, 1000)
p2=GPIO.PWM(enb, 1000)
p.start(ena)
p2.start(enb)

p.ChangeDutyCycle(80)#speed
p2.ChangeDutyCycle(80)#speed
GPIO.output(pin1,True)
GPIO.output(pin2,False)
GPIO.output(pin3,True)
GPIO.output(pin4,False)

