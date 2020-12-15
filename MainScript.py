import time
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

mpu = mpu6050(0x68)

while (gyro_data['x'] == 0){ 
    ##we can change these numbers later. It is more of a structure.
    #move forward
}