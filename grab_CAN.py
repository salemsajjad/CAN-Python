import serial
import time

SerialObj = serial.Serial('COM16')

SerialObj.baudrate = 115200
SerialObj.bytesize = 8
SerialObj.parity = 'N'
SerialObj.stopbits = 1
values = bytearray([80, 0, 26, 1, 90, 255])
time.sleep(3)

while(1):
    srialByte = SerialObj.read(400)
    srialIntList = list(srialByte)
    srialHexList = []
    for byte in srialIntList:
        srialHexList.append(hex(byte))
    try:
        xc2_index = srialIntList.index(194, 0, 399)
    except Exception as e:
        print(e)
    if srialIntList[xc2_index - 1] != 1:
        continue
    speed_list = []
    for i in range(-1, 8):
        speed_list.append(srialIntList[xc2_index + i])
    # print(speed_list)
    vehicle_speed = speed_list[4]
    print(f"the vehicle speed is: {vehicle_speed} km/h")
    try:
        x90_index = srialIntList.index(144, 0, 399)
    except Exception as e:
        print(e)
    if srialIntList[x90_index - 1] != 1:
        continue
    steering_wheel_list = []
    for i in range(-1, 8):
        steering_wheel_list.append(srialIntList[x90_index + i])
    # print(steering_wheel_list)
    steering_wheel = steering_wheel_list[4] *256 + steering_wheel_list[5]
    steering_wheel_deg = (steering_wheel - 32767) * 0.1
    # print(f"steering wheel is : {steering_wheel_deg}")
    # SerialObj.write(values)
    time.sleep(0.01)