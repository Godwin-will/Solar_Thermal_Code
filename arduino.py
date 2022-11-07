import pandas as pd
import serial
import time

# See "Using Python and an Arduino to Read a Sensor "
# https://pythonforundergradengineers.com/python-arduino-potentiometer.html

# Data points can be plotted by the arduino_plot.py script (needs to run in parallel)


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM7', 115200, timeout=1)
time.sleep(2)

def write_data():
    '''
    Reads live data from Arduino and writes them into the data.csv file
    '''
    data = pd.DataFrame()
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        string = string.split(",")  # split string into list
        print(string)
        try:
            if string[0] == 'M>':
                new_data = pd.DataFrame([string[1:6]]).set_index(0)
                data = pd.concat([data, new_data])
                data.to_csv('data.csv', mode='a', header=False)
        except Exception as e:
            print('error:', e)

# run the function write_data() until interrupted by keyboard (Ctrl-C)
try:
    while True:
        write_data()
except KeyboardInterrupt:
    print('interrupted!')

ser.close()