import smbus
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
	#write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    
bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

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

p=GPIO.PWM(ena, 100)
p2=GPIO.PWM(enb, 100)
p.start(ena)
p2.start(enb)



firststage = True
secondstage = False
thirdstage = False
counter = 0

p.ChangeDutyCycle(70)#speed
p2.ChangeDutyCycle(70)#speed
GPIO.output(pin1,True)
GPIO.output(pin2,False)
GPIO.output(pin3,True)
GPIO.output(pin4,False)

while (firststage == True):
    ##we can change these numbers later. It is more of a structure.
    #move forward
    acc_y = read_raw_data(ACCEL_YOUT_H)
    Ay = acc_y/16384.0
    print(Ay*10)
    if (Ay*10 > 4):
        firststage = False
        secondstage = True
        print("moving to second")
    
while (secondstage == True):
    acc_y2 = read_raw_data(ACCEL_YOUT_H)
    Ay2 = acc_y2/16384.0
    print(Ay*10)
    if (Ay2*10< 3):
        print("moving to third")
        secondstage = False
        thirdstage = True

while (thirdstage == True):
    while (counter <= 1400):
        print("3rd")
        counter += 1
    thirdstage = False
p.ChangeDutyCycle(80)#speed
p2.ChangeDutyCycle(80)#speed
GPIO.output(pin1,False)
GPIO.output(pin2, False)
GPIO.output(pin3,False)
GPIO.output(pin4, False)