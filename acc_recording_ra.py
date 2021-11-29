# Python script to record the ADXL345 accelerometer data into a text file.
# Author: Narutoshi Nakata
# License: Tokushima University
# branch_testと計測開始時刻の出力
import os
import time
from datetime import datetime

# Import the ADXL345 module.
import Adafruit_ADXL345

#計測開始時刻を出力する
now = datetime.now()
now2 = str(now)+"\n" #str型に変更し、改行する
#now3 = str(datetime.now()) + "\n"
filename = "data"+now.strftime("%Y-%m-%d_%H-%M")+".txt"
print(filename)

#ファイル名をdata+連番.txtとする
dir = '../data'
count_file = sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir))
#print(count_file)
filename = "data"+str(count_file)+".txt"
print(filename)

# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345(address=0x1d, busnum=1)

# You can optionally change the range to one of:
#  - ADXL345_RANGE_2_G   = +/-2G (default)
#  - ADXL345_RANGE_4_G   = +/-4G
#  - ADXL345_RANGE_8_G   = +/-8G
#  - ADXL345_RANGE_16_G  = +/-16G
# For example to set to +/- 16G:
accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_16_G)
G = 9.80665
sf = float((4/1000) * G)
print(sf)

# Or change the data rate to one of:
#  - ADXL345_DATARATE_0_10_HZ = 0.1 hz
#  - ADXL345_DATARATE_0_20_HZ = 0.2 hz
#  - ADXL345_DATARATE_0_39_HZ = 0.39 hz
#  - ADXL345_DATARATE_0_78_HZ = 0.78 hz
#  - ADXL345_DATARATE_1_56_HZ = 1.56 hz
#  - ADXL345_DATARATE_3_13_HZ = 3.13 hz
#  - ADXL345_DATARATE_6_25HZ  = 6.25 hz
#  - ADXL345_DATARATE_12_5_HZ = 12.5 hz
#  - ADXL345_DATARATE_25_HZ   = 25 hz
#  - ADXL345_DATARATE_50_HZ   = 50 hz
#  - ADXL345_DATARATE_100_HZ  = 100 hz (default)
#  - ADXL345_DATARATE_200_HZ  = 200 hz
#  - ADXL345_DATARATE_400_HZ  = 400 hz
#  - ADXL345_DATARATE_800_HZ  = 800 hz
#  - ADXL345_DATARATE_1600_HZ = 1600 hz
#  - ADXL345_DATARATE_3200_HZ = 3200 hz
# For example to set to 6.25 hz:
accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_800_HZ)

F = open('../data/'+filename,'w')
F.write(now2) #計測開始時刻をファイルに出力する
print('Press ctrl-c to stop recording...')
start_time = time.time()
try:
    while True:
        # Read the X, Y, Z axis acceleration values and print them.
        x, y, z = accel.read()
        elapsed_time=time.time()-start_time
        resacc = (((float(x)*sf)**2+(float(y)*sf)**2+(float(z)*sf)**2)**(1/2)) - G
        datastr='{:.3f}'.format(elapsed_time)+"\t"+str(float(x)*sf)+"\t"+str(float(y)*sf)+"\t"+str(float(z)*sf)+"\t"+str(resacc)+"\n"
        F.write(datastr)
        time.sleep(0.0001)
except KeyboardInterrupt:
    F.close()
    print('Data has been successfully saved into a file.')
