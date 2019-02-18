import serial
import sys
import time
ser = serial.Serial('COM3', 115200, timeout=1)


arr=[]
arr.append(b'\x01') 
arr.append(b'\x01')
for i in range(19):
    arr.append(b'\x0f')
arr.append(b'\x16')
print(arr)

for j in arr:
    ser.write(j)
print('done op')

print("sleeping")
time.sleep(0.5)

#------------------------------------------------

arr=[]
arr.append(b'\x01')
arr.append(b'\x00')
for i in range(19):
    arr.append(b'\x01')
arr.append(b'\x16')
print(arr)

for j in arr:
    ser.write(j)
print('done op')

#-------------------------------------------------
##
##print('sleeping')
##time.sleep(1)

print('reading')
i=1

while i:
    
    s = ser.read()        
    s = int.from_bytes(s, byteorder=sys.byteorder)
    print(i,'s is',s)
    i+=1
    if i>22:
        i=0

        
ser.close()
