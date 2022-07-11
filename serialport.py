import serial
import codecs

serialPort = serial.Serial(port = "COM7", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


data_to_compare = [0x45,0x00,0x00,0x00,0x00,0x45]
data_to_send = [0x45,0x11,0x11,0x11,0x11,0x45]
rec_data_list = []

while (1):
    if(serialPort.in_waiting > 0):
        rec_data= serialPort.readline(1)
        #rec_data = codecs.encode(rec_data, "hex") 
        rec_data_list.append(ord(rec_data))
        
        #if (rec_data==data_to_compare):
        
        if(serialPort.in_waiting == 0):            
            #if(rec_data_list == data_to_compare):
            print("they are equal")
            data_to_send[0] = rec_data_list[0]
            data_to_send[5] = rec_data_list[5]
            serialPort.write(serial.to_bytes(data_to_send))
            rec_data_list = []
