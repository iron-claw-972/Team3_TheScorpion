from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

while True:
    accel_data = mpu.get_accel_data()
    print("accel y : " +str(accel_data['y']))
    
    if (accel_data['y'] > 3):
        print("yes")