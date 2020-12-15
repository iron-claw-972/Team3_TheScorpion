import time
import RPi.GPIO as GPIO   
from mpu6050 import mpu6050

mpu = mpu6050(0x68)
